# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CraftIt', '0004_remove_packetdetails_db_srcport'),
    ]

    operations = [
        migrations.AddField(
            model_name='packetdetails',
            name='db_srcPort',
            field=models.IntegerField(null=True),
        ),
    ]
