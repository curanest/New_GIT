# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0003_auto_20161011_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_count', models.IntegerField(default=0, editable=False)),
                ('title', models.CharField(max_length=70)),
                ('couponcode', models.CharField(max_length=10)),
                ('slug', models.CharField(max_length=20)),
                ('trainer', models.CharField(max_length=20)),
                ('sme', models.CharField(max_length=20)),
                ('level', models.CharField(choices=[(b'Micro', b'micro'), (b'Foundation', b'foundation'), (b'Advance', b'advance')], max_length=10)),
                ('overview', models.TextField()),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to=b'photos/%Y/%m/%d')),
                ('duration', models.CharField(max_length=10)),
                ('participants', models.IntegerField()),
            ],
        ),
    ]
