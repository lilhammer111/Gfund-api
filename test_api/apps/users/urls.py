from .views import UserView
from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh

urlpatterns = [
    path('users/', UserView.as_view()),
    # # jwt登录 就这一行代码,路由名称随便写，这里就写login
    path('token/', token_obtain_pair),
    path('token/refresh/', token_refresh)
]