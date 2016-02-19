# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mape', '0004_auto_20160211_1900'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='commertial_id',
            new_name='commertial',
        ),
        migrations.RenameField(
            model_name='sponsor',
            old_name='event_id',
            new_name='event',
        ),
    ]
