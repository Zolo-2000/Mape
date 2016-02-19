# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mape', '0002_auto_20160211_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='identification',
            field=models.BigIntegerField(max_length=13, null=True, blank=True),
        ),
    ]
