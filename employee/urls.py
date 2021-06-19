from employee.views import EmployeeListCreateView, EmployeeRetrieveUpdateView
from django.urls import path


urlpatterns = [
    path('', EmployeeListCreateView.as_view(), name="employee-list-create"),
    path('<int:id>/', EmployeeRetrieveUpdateView.as_view(),
         name="employee-retrieve-update")
]
