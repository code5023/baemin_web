# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0006_auto_20170114_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='category',
            field=models.CharField(choices=[('ko', '한식'), ('cn', '중식'), ('jp', '일식')], default='ko', max_length=10, verbose_name='음식 종류'),
        ),
    ]
