# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_cuenta_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='user',
        ),
    ]
