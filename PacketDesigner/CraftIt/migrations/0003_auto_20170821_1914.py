# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CraftIt', '0002_auto_20170821_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packetdetails',
            name='db_destIP',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='packetdetails',
            name='db_destPort',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='packetdetails',
            name='db_flags',
            field=models.CharField(blank=True, max_length=6),
        ),
        migrations.AlterField(
            model_name='packetdetails',
            name='db_payload',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='packetdetails',
            name='db_protocol',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='packetdetails',
            name='db_srcIP',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='packetdetails',
            name='db_srcPort',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='packetdetails',
            name='db_summary',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='packetdetails',
            name='db_ttlValue',
            field=models.IntegerField(null=True),
        ),
    ]