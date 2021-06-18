from django.contrib.admin.utils import lookup_field
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from .models import Client,ClientAddress
from .serializers import ClientSerializer,ClientAddressSerializer


class ClientListView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^name']
    permission_classes = [IsAuthenticated]


class ClientDetailView(RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"


class ClientAddressListView(ListCreateAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def perform_create(self, serializer):
        try:
            field=self.lookup_field
            client = Client.objects.get(pk=self.kwargs[field])
        except Client.DoesNotExist:
            client=None
        serializer.save(owner=client)

class ClientAddressDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

