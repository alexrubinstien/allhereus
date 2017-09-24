# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20170816_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parent_email',
            field=models.EmailField(blank=True, help_text='Contact email for parent or guardian.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]