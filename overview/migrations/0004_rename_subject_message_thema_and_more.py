# Generated by Django 4.0.6 on 2022-07-09 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0003_message_alter_bookings_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='subject',
            new_name='thema',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='duration',
            new_name='dauer',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='group',
            new_name='groupe',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='price',
            new_name='preis',
        ),
        migrations.RemoveField(
            model_name='bookings',
            name='customerName',
        ),
        migrations.RemoveField(
            model_name='bookings',
            name='time',
        ),
        migrations.AddField(
            model_name='bookings',
            name='dauer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookings',
            name='nachname',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='bookings',
            name='nummer',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookings',
            name='preis',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookings',
            name='service',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='bookings',
            name='uhrzeit',
            field=models.DateTimeField(default=datetime.date.today(), unique=True),
        ),
        migrations.AddField(
            model_name='bookings',
            name='vorname',
            field=models.CharField(default='', max_length=255),
        ),
    ]
