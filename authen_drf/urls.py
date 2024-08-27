from django.urls import path

from authen_drf.apps import AuthenDrfConfig
from authen_drf.views import *

app_name = AuthenDrfConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='list'),
    path('<int:pk>', UserRetrieveAPIView.as_view(), name='detal'),
    path('<int:pk>/update', UserUpdateAPIView.as_view(), name='update'),
    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('<int:pk>/delete', UserDestroyAPIView.as_view(), name='delete'),
]
