# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-06 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimientos', '0002_ventanueva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventanueva',
            name='service',
            field=models.IntegerField(choices=[(3, 'Plata'), (4, 'Oro'), (5, 'Oro HD'), (10, 'Oro HD Plus'), (10, 'Platino'), (10, 'Nexus')], default=5),
        ),
    ]
