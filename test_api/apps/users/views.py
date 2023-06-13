from rest_framework.generics import CreateAPIView
from .serializers import CreateUserSerializer


# Create your views here.
class UserView(CreateAPIView):
    serializer_class = CreateUserSerializer

