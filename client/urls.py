from django.urls import path
from client.views import ClientListView,ClientDetailView,ClientAddressListView,ClientAddressDetailView


urlpatterns = [
    path('',ClientListView.as_view(),name='client-list'),
    path('<int:id>',ClientDetailView.as_view(),name='client-operations'),
    path('<int:id>/address',ClientAddressListView.as_view(),name='client-address-list'),
    path('address/<int:id>',ClientAddressDetailView.as_view(),name='client-address-list-operations'),
]