# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-13 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cathegory', '0006_auto_20180613_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
