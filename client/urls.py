from django.urls import path
from .views import(ClientListCreateView,
                   ClientRetrieveUpdateView,
                   ClientAddressListCreateView,
                   ClientAddressRetrieveUpdateDestroyView,
                   ClientServiceListCreateView,
                   ClientServiceRetrieveUpdateDestroyView)


urlpatterns = [
    path('', ClientListCreateView.as_view(), name='client-list'),
    path('<int:id>/', ClientRetrieveUpdateView.as_view(), name='client-operations'),
    path('<int:id>/address/', ClientAddressListCreateView.as_view(),
         name='client-address-list/'),
    path('address/<int:id>/', ClientAddressRetrieveUpdateDestroyView.as_view(),
         name='client-address-list-operations'),
    path('<int:id>/sevice/', ClientServiceListCreateView.as_view(),
         name='client-service-list/'),
    path('service/<int:id>/', ClientServiceRetrieveUpdateDestroyView.as_view(),
         name='client-service-list-operations'),
]