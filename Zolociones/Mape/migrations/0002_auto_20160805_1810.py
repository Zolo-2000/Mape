# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mape', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='categorie',
            new_name='categories',
        ),
        migrations.RemoveField(
            model_name='commertial',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='commertial',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='hashtag',
            name='image',
        ),
        migrations.AddField(
            model_name='offer',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
        migrations.AddField(
            model_name='sponsor',
            name='state',
            field=models.IntegerField(default=20, choices=[(10, b'approved'), (20, b'pending')]),
        ),
        migrations.AlterField(
            model_name='commertial',
            name='commertial_name',
            field=models.CharField(unique=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.ImageField(null=True, upload_to=b'media', blank=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='offers',
            field=models.ManyToManyField(to='Mape.Offer', blank=True),
        ),
    ]
