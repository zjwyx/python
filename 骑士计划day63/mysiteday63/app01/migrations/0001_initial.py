# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2020-10-22 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
    ]
