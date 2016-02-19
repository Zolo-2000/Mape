# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mape', '0008_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='cover_image',
            field=models.ImageField(null=True, upload_to=b'media_event'),
        ),
        migrations.AlterField(
            model_name='commertial',
            name='commertial_image',
            field=models.ImageField(upload_to=b'media_commertial'),
        ),
        migrations.AlterField(
            model_name='commertial',
            name='date_joined',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='state',
            field=models.IntegerField(max_length=1, choices=[(b'10', b'Public'), (b'20', b'Private'), (b'21', b'Whit invitation'), (b'12', b'Public is coming'), (b'22', b'Private is coming'), (b'13', b'Public Canceled'), (b'23', b'Private Canceled'), (b'14', b'Public Completed'), (b'24', b'Private Completed')]),
        ),
    ]
