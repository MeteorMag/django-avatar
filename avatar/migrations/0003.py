# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 15:48
from __future__ import unicode_literals

import avatar.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avatar', '0002_add_verbose_names_to_avatar_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='avatar',
            field=avatar.models.AvatarField(),
        ),
    ]
