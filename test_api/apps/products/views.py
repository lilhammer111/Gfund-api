from django.contrib.auth.models import AnonymousUser
from rest_framework.viewsets import ModelViewSet
from .models import Product
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import BasePermission
from test_api.settings.dev import PERMISSIONS


# Create your views here.

class ProductsPermission(BasePermission):
    def has_permission(self, request, view):
        # 当前用户所配置的权限
        if isinstance(request.user, AnonymousUser):
            print('匿名用户请求')
            return False
        permission = PERMISSIONS[request.user.role]
        # 当前用户正在访问的url名称以及访问方式
        url_name = request.resolver_match.url_name
        # 权限校验逻辑
        methods = permission.get(url_name)
        if not methods or request.method not in methods:
            return False
        return True


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # ProductsPermission,
    # permission_classes = [IsAuthenticated]
