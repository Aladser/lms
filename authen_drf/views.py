from rest_framework import generics
from rest_framework.permissions import AllowAny

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

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()

class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserDetailSerializer

    queryset = User.objects.all()
    permission_classes = (IsPersonalProfilePermission,)

class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
