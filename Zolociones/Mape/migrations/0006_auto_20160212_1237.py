# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Mape', '0005_auto_20160211_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commertial_offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commertial', models.ForeignKey(to='Mape.Commertial')),
                ('offer', models.ForeignKey(to='Mape.Offer')),
            ],
        ),
        migrations.RenameModel(
            old_name='Commertial_categories',
            new_name='Categorie',
        ),
        migrations.RenameModel(
            old_name='Trade_offers',
            new_name='Commertial_categorie',
        ),
        migrations.RenameField(
            model_name='commertial_categorie',
            old_name='commertial_id',
            new_name='commertial',
        ),
        migrations.RemoveField(
            model_name='commertial_categorie',
            name='offer_id',
        ),
        migrations.AddField(
            model_name='commertial_categorie',
            name='categorie',
            field=models.ForeignKey(to='Mape.Categorie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
