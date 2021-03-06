# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-19 22:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awards', '0002_auto_20190319_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.ManyToManyField(blank=True, related_name='content', to=settings.AUTH_USER_MODEL)),
                ('design', models.ManyToManyField(blank=True, related_name='design', to=settings.AUTH_USER_MODEL)),
                ('usability', models.ManyToManyField(blank=True, related_name='usability', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
