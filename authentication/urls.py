from django.urls import path
from .views import RegisterUserView,LoginView,LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='user-create'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('refresh-token', TokenRefreshView.as_view(), name='refresh-token'),
    path('logout/',LogoutView.as_view(),name='user-logout'),
]
