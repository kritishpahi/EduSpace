# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20160624_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='subject',
            field=models.IntegerField(choices=[(1, 'Physics'), (2, 'Chemistry'), (3, 'Projects')]),
        ),
    ]
