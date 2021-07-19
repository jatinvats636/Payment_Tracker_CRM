from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter

from .models import Client, ClientAddress,ClientService
from .serializers import ClientSerializer, ClientAddressSerializer,ClientServiceSerializer


class ClientListCreateView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['^name']
    # permission_classes = [IsAuthenticated]


class ClientRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = "id"


class ClientAddressListCreateView(ListCreateAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def perform_create(self, serializer):
        try:
            field = self.lookup_field
            client = Client.objects.get(pk=self.kwargs[field])
        except Client.DoesNotExist:
            client = None
        serializer.save(owner=client)


class ClientAddressRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

class ClientServiceListCreateView(ListCreateAPIView):
    queryset = ClientService.objects.all()
    serializer_class = ClientServiceSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"

    def perform_create(self, serializer):
        try:
            field = self.lookup_field
            client = Client.objects.get(pk=self.kwargs[field])
        except Client.DoesNotExist:
            client = None
        serializer.save(owner=client)


class ClientServiceRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ClientService.objects.all()
    serializer_class = ClientServiceSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"