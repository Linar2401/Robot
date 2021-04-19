# Generated by Django 3.2 on 2021-04-17 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0003_auto_20210417_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='time_arrived',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 20, 47, 45, 599165)),
        ),
        migrations.AlterField(
            model_name='package',
            name='time_of_departure',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 17, 20, 47, 45, 599165)),
        ),
        migrations.AlterField(
            model_name='robotstatus',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 20, 47, 45, 600165)),
        ),
    ]
