# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0007_remove_node_messages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='connections',
        ),
    ]
