# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mape', '0010_auto_20160213_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='state',
            field=models.IntegerField(choices=[(b'10', b'Public'), (b'20', b'Private'), (b'21', b'Whit invitation'), (b'12', b'Public is coming'), (b'22', b'Private is coming'), (b'13', b'Public Canceled'), (b'23', b'Private Canceled'), (b'14', b'Public Completed'), (b'24', b'Private Completed')]),
        ),
    ]
