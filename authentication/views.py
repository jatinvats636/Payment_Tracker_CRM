import datetime
from django.contrib import auth
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomSessionModel
from .serializers import UserSerializer,LoginSerializer,LogoutSerializer


class RegisterUserView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)
            data = {'user': serializer.data,'refresh': str(refresh),'access': str(refresh.access_token)}
            try:
                new_session = CustomSessionModel.objects.create(owner=user,login_time=datetime.datetime.now())
                new_session.save()
            except Exception as e:
                return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(data, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class LogoutView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request):
        serializer=LogoutSerializer(data=request.data)
        if serializer.is_valid():
            try:
                closing_session=CustomSessionModel.objects.get(owner=request.user,is_active=True)
                closing_session.logout_time=datetime.datetime.now()
                closing_session.is_active=False
                closing_session.save()
            except Exception as e:
                return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
