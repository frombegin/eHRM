# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 10:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='password',
        ),
    ]
