# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-08 05:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('statement', models.TextField()),
                ('in_example', models.TextField(max_length=200)),
                ('out_example', models.TextField(max_length=200)),
            ],
        ),
    ]
