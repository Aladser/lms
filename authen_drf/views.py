from datetime import datetime

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from authen_drf.models import User
from authen_drf.permissions import IsPersonalProfilePermission
from authen_drf.serializers import  UserListSerializer, UserDetailSerializer


# --- Пользователь ---
# LIST
class UserListAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


# RETRIEVE
class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        user_obj_pk = self.request.__dict__['parser_context']['kwargs']['pk']
        if user_obj_pk == self.request.user.pk:
            return UserDetailSerializer
        else:
            return UserListSerializer

# CREATE
class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

# UPDATE
class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserDetailSerializer

    queryset = User.objects.all()
    permission_classes = (IsPersonalProfilePermission,)


# DESTROY
class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = (IsPersonalProfilePermission,)

# --- АВТОРИЗАЦИЯ ---
class LoginView(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs) -> Response:

        # обновление времени входа
        authuser = User.objects.get(email=request.data['email'])
        authuser.last_login = datetime.now()
        authuser.save()

        return super().post(request, *args, **kwargs)
