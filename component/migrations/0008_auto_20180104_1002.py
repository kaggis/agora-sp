# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-04 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0007_merge_20170928_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecomponent',
            name='logo',
            field=models.ImageField(default='/var/www/html/agora/static/img/logos/logo-none.jpg', upload_to='/srv/agora/static/img/logos'),
        ),
        migrations.AlterUniqueTogether(
            name='servicedetailscomponent',
            unique_together=set([('service_id', 'service_details_id', 'service_component_implementation_detail_id', 'configuration_parameters')]),
        ),
    ]
