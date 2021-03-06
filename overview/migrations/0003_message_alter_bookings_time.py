# Generated by Django 4.0.6 on 2022-07-07 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('overview', '0002_remove_bookings_phone_remove_bookings_service_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vorname', models.CharField(max_length=255)),
                ('nachname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='bookings',
            name='time',
            field=models.DateTimeField(unique=True),
        ),
    ]
