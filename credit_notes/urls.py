from django.urls import path
from .views import(CreditNotesListCreateView,
        CreditNotesRetrieveUpdateView,
    )

urlpatterns = [
    path('', CreditNotesListCreateView.as_view(), name='credit-notes-list'),
    path('<int:id>/', CreditNotesRetrieveUpdateView.as_view(), name='credit-notes-operations'),
]