# Generated by Django 2.0.3 on 2019-09-10 13:43

from django.db import migrations, models
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0007_auto_20180108_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='type',
            field=models.CharField(choices=[('fixed', 'PHP'), ('percentage', '%')], default='fixed', max_length=10),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='discount_value_type',
            field=models.CharField(choices=[('fixed', 'PHP'), ('percentage', '%')], default='fixed', max_length=10),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='limit',
            field=django_prices.models.MoneyField(blank=True, currency='PHP', decimal_places=2, max_digits=12, null=True),
        ),
    ]
