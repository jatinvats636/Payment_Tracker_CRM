from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

from .models import Invoice, InvoiceService
from .serializers import InvoiceSerializer, InvoiceServiceSerializer


class InvoiceListCreateView(ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^client']
    permission_classes = [IsAuthenticated]


class InvoiceRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class InvoiceServiceListCreateView(ListCreateAPIView):
    queryset = InvoiceService.objects.all()
    serializer_class = InvoiceServiceSerializer
    permission_classes = [IsAuthenticated]
    # lookup_field = "id"


class InvoiceServiceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = InvoiceService.objects.all()
    serializer_class = InvoiceServiceSerializer
    permission_classes = [IsAuthenticated]
    # lookup_field = "id"
