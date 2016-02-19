# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Mape', '0006_auto_20160212_1237'),
    ]

    operations = [
    migrations.RenameField(
        model_name='event',
            old_name='user_id',
            new_name='user'
        ),
        migrations.AlterField(
            model_name='commertial',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
