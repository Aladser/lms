from django.urls import path

from authen_drf.views import UserListAPIView, UserUpdateAPIView, UserRetrieveAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('<int:pk>', UserRetrieveAPIView.as_view(), name='user_detal'),
    path('<int:pk>/update', UserUpdateAPIView.as_view(), name='user_update'),
]
