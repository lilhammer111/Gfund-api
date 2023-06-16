# Generated by Django 4.2.2 on 2023-06-13 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='产品名')),
                ('strategy', models.CharField(max_length=50, verbose_name='策略')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='成立时间')),
                ('principal', models.DecimalField(decimal_places=8, max_digits=20, verbose_name='总投资金额')),
                ('monetary_unit', models.CharField(max_length=15, verbose_name='币种')),
                ('settlement_mode', models.CharField(max_length=50, verbose_name='结算方式')),
                ('revenue_sharing_mode', models.CharField(max_length=50, verbose_name='分成方式')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品',
                'db_table': 'tb_products',
            },
        ),
    ]