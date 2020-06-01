# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-07-15 09:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceThresholdChange',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('done', models.BooleanField(default=False, verbose_name='\u5df2\u7ecf\u63d0\u9192\u8fc7')),
                ('threshold', models.FloatField()),
                ('increase', models.BooleanField(verbose_name='\u4e0a\u6da8\u8fd8\u662f\u4e0b\u8dcc')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='threshold_change', to=settings.AUTH_USER_MODEL, verbose_name='\u521b\u5efa\u8005')),
            ],
            options={
                'db_table': 'eosram_price_threshold_change',
            },
        ),
    ]
