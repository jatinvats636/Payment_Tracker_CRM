from django.urls import path
from .views import ClientListCreateView, ClientRetrieveUpdateView, ClientAddressListCreateView, ClientAddressRetrieveUpdateDestroyView


urlpatterns = [
    path('', ClientListCreateView.as_view(), name='client-list'),
    path('<int:id>/', ClientRetrieveUpdateView.as_view(), name='client-operations'),
    path('<int:id>/address/', ClientAddressListCreateView.as_view(),
         name='client-address-list/'),
    path('address/<int:id>/', ClientAddressRetrieveUpdateDestroyView.as_view(),
         name='client-address-list-operations'),
]
