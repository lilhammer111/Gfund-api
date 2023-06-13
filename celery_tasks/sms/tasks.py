from ronglian_sms_sdk import SmsSDK
from celery_tasks.main import celery_app

accId = '2c94811c8853194e0188a3d14dda16dd'
accToken = '59fed65855ef44efab53eb2e32bacb48'
appId = '2c94811c8853194e0188a3d14f1816e4'


# 使用装饰器注册任务
@celery_app.task(name='send_msg_code')
def send_msg_code(phone, sms_code):
    """
    发送短信的celery异步任务
    :param sms_code:验证码
    :param phone:手机号
    :return:
    """
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    # sms_code为 '5' 表示过期时间为5分钟
    datas = (sms_code, '5')
    sdk.sendMessage(tid, phone, datas)
