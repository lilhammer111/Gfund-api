"""
URL configuration for test_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views

# from rest_framework.routers import SimpleRouter
# router = SimpleRouter()
from rest_framework.routers import SimpleRouter
from products.views import ProductView
# from users.views import UserView
# from rest_framework_simplejwt.views import token_obtain_pair
router = SimpleRouter()
router.register('products', ProductView)
# router.register('users', UserView)
# router.register('login', token_obtain_pair)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_cors/', views.test_cors),
    # 发短信
    path('', include("users.urls")),
    path('', include("verifications.urls")),
    path('', include(router.urls))
]

# urlpatterns += router.urls
