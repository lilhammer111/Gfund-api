from django.db import models


# Create your models here.
class Product(models.Model):
    """产品列表"""
    title = models.CharField(verbose_name='产品名', max_length=50, unique=True)
    strategy = models.CharField(verbose_name='策略', max_length=50, null=True)
    created_time = models.DateTimeField(verbose_name='成立时间', auto_now_add=True)
    principal = models.DecimalField(verbose_name='总投资金额', decimal_places=8, max_digits=20)
    monetary_unit = models.CharField(verbose_name='币种', max_length=15, default='USDT')
    settlement_mode = models.CharField(verbose_name='结算方式', max_length=50)
    revenue_sharing_mode = models.CharField(verbose_name='分成方式', max_length=50)

    class Meta:
        # 配置数据库表名，及设置模型在admin站点显示的中文名
        db_table = 'tb_products'
        verbose_name = '产品'
        verbose_name_plural = verbose_name
