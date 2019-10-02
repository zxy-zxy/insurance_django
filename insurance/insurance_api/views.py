from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response

from insurance_api.serializers import CustomerSerializer, PolicySerializer
from insurance_api.models import Customer, Policy


class CreateCustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CreatePolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.select_related()
    serializer_class = PolicySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            customer = Customer.objects.get(id=kwargs['customer_id'])
        except Customer.DoesNotExist:
            raise Http404

        self.perform_create(serializer, customer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer, customer):
        serializer.save(customer=customer)