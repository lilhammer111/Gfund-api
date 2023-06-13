from rest_framework.viewsets import ModelViewSet
from .models import Product
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import BasePermission


# Create your views here.

class ProductsPermission(BasePermission):
    def has_permission(self, request, view):

        # 权限校验逻辑
        return True


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ProductsPermission]
