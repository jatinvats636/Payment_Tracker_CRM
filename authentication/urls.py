from django.urls import path
from .views import RegisterUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-create'),
    path('login/', TokenObtainPairView.as_view(), name='user-login'),
    path('refresh-token', TokenRefreshView.as_view(), name='refresh-token'),
]
