# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mape', '0009_auto_20160212_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commertial',
            name='latitude',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=15),
        ),
        migrations.AlterField(
            model_name='commertial',
            name='longitude',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=15),
        ),
    ]
