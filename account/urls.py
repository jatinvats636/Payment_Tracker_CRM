from account.views import AccountListCreateView, AccountRetrieveUpdateView
from django.urls import path


urlpatterns = [
    path('', AccountListCreateView.as_view(), name="account-list-create"),
    path('<int:id>/', AccountRetrieveUpdateView.as_view(),
         name="account-retrieve-update")
]
