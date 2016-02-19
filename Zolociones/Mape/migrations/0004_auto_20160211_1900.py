# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Mape', '0003_auto_20160211_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='commertial',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='guests',
            field=models.OneToOneField(to='Mape.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='identification',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
