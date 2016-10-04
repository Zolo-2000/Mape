# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('maccounts', '0002_auto_20160805_1810'),
        ('Mape', '0003_auto_20160914_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='subscribers',
            field=models.ManyToManyField(to='maccounts.User_profile', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='user_profile',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
