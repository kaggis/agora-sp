# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-26 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0027_accesspolicy_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetails',
            name='access_policies',
            field=models.ManyToManyField(blank=True, to='service.AccessPolicy'),
        ),
    ]
