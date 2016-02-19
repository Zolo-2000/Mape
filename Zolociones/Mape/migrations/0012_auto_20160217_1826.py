# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mape', '0011_auto_20160216_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='cover_image',
            field=models.ImageField(null=True, upload_to=b'media_event', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='guests',
            field=models.OneToOneField(null=True, blank=True, to='Mape.Profile'),
        ),
    ]
