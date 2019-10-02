from django.urls import path

from insurance_api.views import CreateCustomerViewSet, CreatePolicyViewSet


create_customer_view_set = CreateCustomerViewSet.as_view(
    {'post': 'create', 'get': 'list'}
)

create_policy_view_set = CreatePolicyViewSet.as_view({'post': 'create', 'get': 'list'})

urlpatterns = [
    path(
        '<version>/create_customer/', create_customer_view_set, name='create_customer'
    ),
    path(
        '<version>/<int:customer_id>/create_policy/',
        create_policy_view_set,
        name='create_policy',
    ),
]
