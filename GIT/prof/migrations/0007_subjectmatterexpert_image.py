# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0006_subjectmatterexpert'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectmatterexpert',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'photos/%Y/%m/%d'),
        ),
    ]
