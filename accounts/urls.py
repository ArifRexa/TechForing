from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterView, CustomTokenObtainPairView, LogoutView, UserDetail, UserList, LogoutAllView, \
    GoogleAuthAPI, UserInfoFromTokenAPI, \
    UpdateUserInfoAPI

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user-info/', UserInfoFromTokenAPI.as_view(), name='user-info-from-token'),
    path('update/', UpdateUserInfoAPI.as_view(), name='user-update'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', UserDetail.as_view()),
]
