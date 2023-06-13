# import re

# from django_redis import get_redis_connection
from rest_framework import serializers
from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """
    需要校验的字段
    default_password为默认值12345678   phone  sms_code
    需要序列化字段：
    id, phone
    需要反序列化的字段：
    default_password phone sms_code
    """
    password = serializers.CharField(label='默认密码', write_only=True)
    # sms_code = serializers.CharField(label='验证码', write_only=True)
    # jwt
    token = serializers.CharField(label='token', read_only=True)

    class Meta:
        model = User
        fields = ['phone', 'id', 'password', 'username', 'token']
        extra_kwargs = {
            'password': {
                'write_only': True,
                # 'min_length': 8,
                'max_length': 16,
                'error_message': {
                    'min_length': '密码仅允许8-16个字符',
                    'max_length': '密码仅允许8-16个字符',
                }
            }
        }
    # 没必要单独校验手机号
    # def validate_phone(self, phone):
    #     """
    #     单独校验手机号
    #     :param phone:str
    #     :return:str
    #     """
    #     if not re.match(r'1[1-3]\d{9}', phone):
    #         raise serializers.ValidationError('手机号格式有误')
    #     return phone

    # def validate(self, attrs):
    #     """
    #     校验两次密码是否相同,以及验证码是否正确
    #     :param attrs: dict
    #     :return: boolean
    #     """
    #     if attrs['password1'] != attrs['password2']:
    #         raise serializers.ValidationError('两次密码不一致')
    #     redis_conn = get_redis_connection('verify_codes')
    #     phone = attrs['phone']
    #     # redis存数据都是字符串，取时是bytes类型，列表则元素为bytes类型
    #     correct_code = redis_conn.get(f'sms_{phone}')
    #     if correct_code is None or attrs['sms_code'] != correct_code.decode():
    #         raise serializers.ValidationError('验证码错误')
    #     return attrs

    def create(self, validated_data):
        # del validated_data['password2']
        # del validated_data['sms_code']
        # del validated_data['allow']
        # 把要删密码先存下来，然后删了再加到模型中
        # password = validated_data.pop('default_password')
        # 下面代码的另一种写法，未验证
        # User.objects.create_user(**validated_data)

        user = User(**validated_data)
        user.set_password(user.password)
        user.save()
        # 在序列化的时候添加token,不存到数据库,只是发给客户端
        from rest_framework_simplejwt.tokens import RefreshToken
        #
        refresh = RefreshToken.for_user(user)
        token = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        user.token = token
        return user



