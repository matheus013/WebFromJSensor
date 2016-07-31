# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0003_application_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('successors', models.TextField()),
                ('current', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='states',
            field=models.TextField(default=[]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stateapp',
            name='ops',
            field=models.TextField(default=[]),
            preserve_default=False,
        ),
    ]
