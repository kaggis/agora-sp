# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-06-05 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0073_auto_20200605_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='erp_fni_1_payment_model',
            field=models.URLField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='resource',
            name='erp_fni_2_pricing',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]
