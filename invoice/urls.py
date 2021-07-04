from django.urls import path
from .views import (InvoiceListCreateView, InvoiceRetrieveUpdateView,
                    InvoiceServiceListCreateView, InvoiceServiceRetrieveUpdateDestroyView)


urlpatterns = [
    path('', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('<int:id>/', InvoiceRetrieveUpdateView.as_view(),
         name='invoice-retrieve-update'),
    path('<int:id>/service/', InvoiceServiceListCreateView.as_view(),
         name='invoice-service-list-create'),
    path('service/<int:id>/', InvoiceServiceRetrieveUpdateDestroyView.as_view(),
         name='invoice-service-list-retrieve-update')
]
