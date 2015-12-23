# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 12:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('remind', '0002_auto_20151223_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='remind',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u521b\u5efa\u8005'),
            preserve_default=False,
        ),
    ]
