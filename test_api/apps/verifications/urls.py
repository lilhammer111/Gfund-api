from django.urls import path,re_path
from .views import SMSCodeView

urlpatterns = [
    re_path(r'^sms_codes/(?P<phone>1[3-9]\d{9})', SMSCodeView.as_view())
]