from celery import Celery

# 1 创建celery实例
celery_app = Celery('my_celery')
# 2 加载配置文件
celery_app.config_from_object('celery_tasks.config')
# 3 自动注册异步任务
celery_app.autodiscover_tasks(['celery_tasks.sms'])
