# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-21 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitydb', '0009_auto_20160616_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprojectagreement',
            name='detailed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectagreement',
            name='detailed',
            field=models.BooleanField(default=False),
        ),
    ]
