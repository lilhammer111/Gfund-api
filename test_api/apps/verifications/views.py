from random import randint
import redis
from rest_framework.response import Response
from rest_framework.views import APIView
from django_redis import get_redis_connection
import logging
from rest_framework import status
from .constants import *
from celery_tasks.sms.tasks import send_msg_code

logger = logging.getLogger('django')


# Create your views here.
class SMSCodeView(APIView):
    """
    短信验证码
    """

    def get(self, request, phone):
        # 1 创建redis连接对象
        redis_conn: redis.Redis = get_redis_connection('verify_codes')
        # 2 获取redis标记
        send_flag = redis_conn.get(f'send_flag_{phone}')
        # 3 频繁发送，返回400
        if send_flag:
            return Response({'msg': '请稍候再发～'}, status=status.HTTP_400_BAD_REQUEST)
        # 4. 生成验证码
        sms_code = '%04d' % randint(0, 999)
        logger.info(sms_code)
        # 5 创建redis管道
        pl = redis_conn.pipeline()
        # 存验证码至redis
        pl.setex(f'sms_{phone}', SMS_CODE_REDIS_EXPIRES, sms_code)
        # 存储一个标记，表示已发送过短信， 60s
        pl.setex(f'send_flag_{phone}', SEND_SMS_CODE_INTERVAL, 1)
        # 执行管道
        pl.execute()
        # 6 将利用容联云通讯发送短信验证码的任务添加到celery
        send_msg_code.delay(phone, sms_code)
        # 7 响应
        return Response({'msg': 'code_msg sends successfully'})
