# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(max_length=128)),
                ('password', models.TextField()),
                ('name', models.TextField()),
                ('surname', models.TextField()),
                ('city', models.TextField()),
            ],
        ),
    ]