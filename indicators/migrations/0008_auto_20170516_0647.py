# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-16 13:47
from __future__ import unicode_literals

from django.db import migrations


def PopulateLevelCreatedDateField(apps, schema_editor):
    level_model = apps.get_model("indicators", "Level")
    levels = level_model.objects.all()

    for l in levels:
        if l.name == 'Goal':
            l.create_date = '2015-10-03 19:03:50'
        elif l.name == 'Output':
            l.create_date = '2015-10-03 19:03:52'
        elif l.name == 'Outcome':
            l.create_date = '2015-10-03 19:03:51'
        elif l.name == 'Activity':
            l.create_date = '2015-10-03 19:03:53'
        elif l.name == 'Impact':
            l.create_date = '2015-10-03 19:03:54'
        l.save()


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0007_auto_20170510_0749'),
    ]

    operations = [
        migrations.RunPython(PopulateLevelCreatedDateField),
    ]
