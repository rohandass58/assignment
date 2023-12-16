# Generated by Django 5.0 on 2023-12-16 03:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_api', '0003_alter_studentdetails_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='dob',
            field=models.DateField(default=datetime.datetime(2023, 12, 16, 3, 21, 23, 555610)),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='enrollment_id',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]