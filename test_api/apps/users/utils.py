# from django.contrib.auth.models import update_last_login
from datetime import datetime, timedelta
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.settings import api_settings


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['role'] = user.role
        # Set expire time to 30 minutes
        token['exp'] = datetime.utcnow() + timedelta(minutes=30)

        return token
    #
    # def validate(self, attrs):
    #     data = super().validate(attrs)
    #
    #     refresh = self.get_token(self.user)
    #
    #     data["refresh"] = str(refresh)
    #     data["access"] = str(refresh.access_token)
    #     data['username'] = self.user.username
    #     data['role'] = self.user.role
    #
    #     if api_settings.UPDATE_LAST_LOGIN:
    #         update_last_login(None, self.user)
    #
    #     return data
