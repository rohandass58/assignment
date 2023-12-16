# Generated by Django 5.0 on 2023-12-16 14:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_api', '0006_alter_academicdetails_date_of_joining_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='class_name',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentdetails',
            name='session',
            field=models.IntegerField(blank=True, default='2023', null=True),
        ),
        migrations.AlterField(
            model_name='academicdetails',
            name='date_of_joining',
            field=models.DateField(default=datetime.datetime(2023, 12, 16, 14, 42, 35, 221470)),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='dob',
            field=models.DateField(default=datetime.datetime(2023, 12, 16, 14, 42, 35, 220487)),
        ),
    ]
