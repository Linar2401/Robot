# Generated by Django 3.2 on 2021-04-22 17:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0014_auto_20210422_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='time_arrived',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 22, 17, 4, 11, 275237)),
        ),
        migrations.AlterField(
            model_name='package',
            name='time_of_departure',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 22, 17, 4, 11, 275251)),
        ),
        migrations.AlterField(
            model_name='position',
            name='time_info_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 22, 17, 4, 11, 274914)),
        ),
        migrations.AlterField(
            model_name='robotstatus',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 22, 17, 4, 11, 275560)),
        ),
    ]
