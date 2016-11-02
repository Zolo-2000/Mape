# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maccounts', '0002_auto_20160805_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='activation_key',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='key_expires',
            field=models.DateTimeField(null=True),
        ),
    ]
