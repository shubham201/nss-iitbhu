# -*- coding: utf-8 -*-
# Generated by Django 1.9.dev20150907194702 on 2015-09-18 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nss_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Funds',
            new_name='Fund',
        ),
        migrations.AlterModelOptions(
            name='camp',
            options={'ordering': ['camp_type']},
        ),
        migrations.AlterModelOptions(
            name='family',
            options={'ordering': ['head_name']},
        ),
        migrations.AlterModelOptions(
            name='fund',
            options={'ordering': ['source']},
        ),
        migrations.AlterModelOptions(
            name='village',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='volunteer',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='camp',
            name='camp_type',
            field=models.CharField(max_length=20, blank=False),
        ),
        migrations.AddField(
            model_name='family',
            name='head_name',
            field=models.CharField(max_length=20, blank=False),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='volunteer_id',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
