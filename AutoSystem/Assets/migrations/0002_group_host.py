# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-17 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20)),
                ('group_desc', models.CharField(blank='Ture', max_length=200, null='Ture')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=20)),
                ('host_nip', models.CharField(max_length=16)),
                ('host_wip', models.CharField(blank='Ture', max_length=16, null='Ture')),
                ('host_desc', models.CharField(blank='Ture', max_length=200, null='Ture')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assets.group')),
            ],
        ),
    ]
