# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-26 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wagtailimages.Image'),
        ),
    ]
