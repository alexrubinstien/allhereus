# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-07-19 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_intervention_strategies'),
    ]

    operations = [
        migrations.AddField(
            model_name='strategy',
            name='evidence_of_success',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='strategy',
            name='family_actions',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='strategy',
            name='materials',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='strategy',
            name='objective',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='strategy',
            name='other_resources_downloads',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='strategy',
            name='other_resources_links',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='strategy',
            name='quick_tips',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='strategy',
            name='root_cause_domains',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='strategy',
            name='staff_actions_after',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='strategy',
            name='staff_actions_before',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='strategy',
            name='student_actions',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='strategy',
            name='student_grouping',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='strategy',
            name='watch_out_for',
            field=tinymce.models.HTMLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='description',
            field=models.TextField(help_text='Expository text about the Strategy; used in page views to elaborate on the Strategy beyond what is in the display_name.'),
        ),
    ]
