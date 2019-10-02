from _datetime import datetime

from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from insurance_api.models import Customer, Policy


class CreateCustomerTest(TestCase):
    def setUp(self):
        self.content_type = 'application/json'

        self.valid_customer_data = {
            'first_name': 'Red',
            'last_name': 'Plum',
            'dob': '2019-10-02',
        }

        self.invalid_customer_data = {
            'first_name': 'Red',
            'last_name': 'Plum',
            'dob': 'invalid date',
        }

    def test_create_customer_passed(self):
        response = self.client.post(
            reverse('create_customer', args=['v1']),
            data=self.valid_customer_data,
            content_type=self.content_type,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)

    def test_create_customer_raised_error(self):
        response = self.client.post(
            reverse('create_customer', args=['v1']),
            data=self.invalid_customer_data,
            content_type=self.content_type,
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Customer.objects.count(), 0)


class CreatePolicyTest(TestCase):
    def setUp(self):
        self.content_type = 'application/json'

        self.valid_policy_data = {
            'type': 'extra',
            'cover': 1000,
            'premium': 1000,
        }

    def test_create_policy_passed(self):
        customer = Customer.objects.create(
            first_name='red', last_name='plum', dob=datetime.now().date()
        )
        response = self.client.post(
            reverse('create_policy', args=['v1', customer.id]),
            data=self.valid_policy_data,
            content_type=self.content_type,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Policy.objects.count(), 1)

    def test_create_policy_for_non_existing_user_raises_error(self):
        customer_id = 100500
        response = self.client.post(
            reverse('create_policy', args=['v1', customer_id]),
            data=self.valid_policy_data,
            content_type=self.content_type,
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Policy.objects.count(), 0)
