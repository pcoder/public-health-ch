# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 15:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('home', '0023_contact_home_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialcontact',
            name='home_site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Site'),
        ),
    ]
