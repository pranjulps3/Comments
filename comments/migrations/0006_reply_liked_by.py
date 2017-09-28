# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-28 12:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0005_auto_20170916_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_reply', to=settings.AUTH_USER_MODEL),
        ),
    ]
