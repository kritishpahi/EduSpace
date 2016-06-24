# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20160624_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Explanation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topics', models.CharField(max_length=100)),
                ('theory', models.TextField()),
                ('details', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='details',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='theory',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='topics',
        ),
        migrations.AddField(
            model_name='explanation',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Subjects'),
        ),
    ]
