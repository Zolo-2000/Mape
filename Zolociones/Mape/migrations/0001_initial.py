# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maccounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categorie_name', models.CharField(unique=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Commertial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commertial_name', models.CharField(max_length=45)),
                ('ruc', models.BigIntegerField(null=True, blank=True)),
                ('description', models.TextField()),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('commertial_image', models.ImageField(upload_to=b'accounts')),
                ('latitude', models.DecimalField(null=True, max_digits=19, decimal_places=15)),
                ('longitude', models.DecimalField(null=True, max_digits=19, decimal_places=15)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_name', models.CharField(max_length=75)),
                ('info', models.TextField()),
                ('when', models.DateTimeField()),
                ('ends', models.DateTimeField(null=True, blank=True)),
                ('cover_price', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('cover_image', models.ImageField(null=True, upload_to=b'media_event', blank=True)),
                ('state', models.IntegerField(default=20, choices=[(10, b'Public'), (20, b'Private'), (21, b'Whit invitation'), (12, b'Public is coming'), (22, b'Private is coming'), (221, b'Private with invitation is coming'), (13, b'Public Completed'), (23, b'Private Completed'), (14, b'Public Canceled'), (24, b'Private Canceled'), (244, b'Private with invitation is canceled')])),
                ('date_joined', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hashtag_name', models.CharField(max_length=45)),
                ('image', models.ImageField(null=True, upload_to=b'media', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location_name', models.CharField(max_length=45)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=b'media')),
                ('latitude', models.DecimalField(null=True, max_digits=19, decimal_places=15)),
                ('longitude', models.DecimalField(null=True, max_digits=19, decimal_places=15)),
                ('categorie', models.ManyToManyField(to='Mape.Categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('offer_name', models.CharField(unique=True, max_length=45)),
                ('price', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('product', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(null=True, upload_to=b'media_event', blank=True)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('state', models.IntegerField(choices=[(10, b'Event image'), (20, b'Commertial image'), (30, b'Hashtag image')])),
                ('event', models.ForeignKey(to='Mape.Event')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('commertial', models.ForeignKey(to='Mape.Commertial')),
                ('event', models.ForeignKey(to='Mape.Event')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='offers',
            field=models.ManyToManyField(to='Mape.Offer'),
        ),
        migrations.AddField(
            model_name='location',
            name='user_profile',
            field=models.ForeignKey(to='maccounts.User_profile'),
        ),
        migrations.AddField(
            model_name='event',
            name='hashtags',
            field=models.ManyToManyField(to='Mape.Hashtag'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(blank=True, to='Mape.Location', null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commertial',
            name='location',
            field=models.OneToOneField(to='Mape.Location'),
        ),
        migrations.AddField(
            model_name='commertial',
            name='user_profile',
            field=models.OneToOneField(to='maccounts.User_profile'),
        ),
    ]
