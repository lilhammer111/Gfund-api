from django.urls import path
from .views import UserView
# from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_simplejwt.views import token_obtain_pair

urlpatterns = [
    path('users/', UserView.as_view()),
    # jwt登录 就这一行代码,路由名称随便写，这里就写login
    # path('login/', token_obtain_pair)
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', token_obtain_pair)
]
