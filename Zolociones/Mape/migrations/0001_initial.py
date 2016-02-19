# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commertial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_joined', models.DateField()),
                ('commertial_image', models.ImageField(upload_to=b'media_profile')),
                ('latitude', models.DecimalField(max_digits=19, decimal_places=15)),
                ('longitude', models.DecimalField(max_digits=19, decimal_places=15)),
                ('price_initial', models.DecimalField(max_digits=9, decimal_places=2)),
                ('price_final', models.DecimalField(max_digits=9, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Commertial_categories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('when', models.DateField()),
                ('ends', models.DateField()),
                ('state', models.IntegerField()),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('guests', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('charter', models.CharField(max_length=13, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'media_profile', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commertial_id', models.ForeignKey(to='Mape.Commertial')),
                ('event_id', models.ForeignKey(to='Mape.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Trade_offers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commertial_id', models.ForeignKey(to='Mape.Commertial')),
                ('offer_id', models.ForeignKey(to='Mape.Offer')),
            ],
        ),
    ]
