# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-22 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Assets', '0006_auto_20160722_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servers_info',
            name='cpu_count',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='servers_info',
            name='cpu_models',
            field=models.CharField(max_length=48),
        ),
        migrations.AlterField(
            model_name='servers_info',
            name='disk_total',
            field=models.IntegerField(max_length=48),
        ),
        migrations.AlterField(
            model_name='servers_info',
            name='kernel_version',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='servers_info',
            name='p_mem',
            field=models.IntegerField(max_length=48),
        ),
        migrations.AlterField(
            model_name='servers_info',
            name='system_type',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='servers_info',
            name='v_mem',
            field=models.IntegerField(max_length=48),
        ),
    ]
