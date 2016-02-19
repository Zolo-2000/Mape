# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mape', '0012_auto_20160217_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ends',
            field=models.DateField(null=True, blank=True),
        ),
    ]
