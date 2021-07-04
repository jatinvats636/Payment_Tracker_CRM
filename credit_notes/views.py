from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import CreditNotes
from .serializers import CreditNotesSerializer

class CreditNotesListCreateView(ListCreateAPIView):
    queryset = CreditNotes.objects.all()
    serializer_class = CreditNotesSerializer
    permission_classes = [IsAuthenticated]


class CreditNotesRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = CreditNotes.objects.all()
    serializer_class = CreditNotesSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"