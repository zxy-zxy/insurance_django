from rest_framework import serializers

from insurance_api.models import Customer, Policy


class CustomerSerializer(serializers.ModelSerializer):
    policies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'dob', 'policies']
        read_only_fields = ('id', 'policies')


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ['id', 'customer_id', 'type', 'premium', 'cover']
        read_only_fields = ('id', 'customer_id')
