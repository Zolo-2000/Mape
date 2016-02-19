# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mape', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='charter',
            new_name='user_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='identification',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
