# -*- coding: utf-8 -*-
# Generated by Django 1.9.dev20150907194702 on 2015-10-12 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nss_app', '0002_auto_20150918_0616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='volunteer_id',
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
    ]