# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kanji', models.CharField(max_length=50)),
                ('skipcode', models.CharField(max_length=50)),
                ('p1', models.CharField(max_length=50)),
                ('p2', models.CharField(max_length=50)),
                ('p3', models.CharField(max_length=50)),
            ],
        ),
    ]
