# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maccounts', '0002_auto_20160805_1810'),
        ('Mape', '0002_auto_20160805_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='guests',
            field=models.ManyToManyField(to='maccounts.User_profile', blank=True),
        ),
        migrations.AlterField(
            model_name='commertial',
            name='commertial_image',
            field=models.ImageField(null=True, upload_to=b'accounts', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='hashtags',
            field=models.ManyToManyField(to='Mape.Hashtag', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(to='Mape.Location', null=True),
        ),
    ]
