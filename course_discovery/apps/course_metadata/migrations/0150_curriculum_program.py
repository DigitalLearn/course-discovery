# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-29 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0149_auto_20190201_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculum',
            name='program',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='curricula', to='course_metadata.Program'),
        ),
    ]
