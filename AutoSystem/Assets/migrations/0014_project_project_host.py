# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-14 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assets', '0013_auto_20160811_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, unique='True')),
                ('sevice_filter_re', models.CharField(max_length=100)),
                ('project_desc', models.CharField(blank='Ture', max_length=200, null='Ture')),
            ],
        ),
        migrations.CreateModel(
            name='project_host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assets.Host')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assets.project', to_field='project_name')),
            ],
        ),
    ]