# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-25 23:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20160822_2337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='post',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]