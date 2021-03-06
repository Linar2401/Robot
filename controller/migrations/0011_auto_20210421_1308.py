# Generated by Django 3.2 on 2021-04-21 13:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0010_auto_20210421_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='position_number',
            field=models.CharField(choices=[('P1', 'Position #1'), ('P2', 'Position #2'), ('P3', 'Position #3'), ('P4', 'Position #4'), ('P5', 'Position #5')], default='P1', max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='time_arrived',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 13, 8, 36, 123463)),
        ),
        migrations.AlterField(
            model_name='package',
            name='time_of_departure',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 21, 13, 8, 36, 123492)),
        ),
        migrations.AlterField(
            model_name='position',
            name='time_info_updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 13, 8, 36, 122430)),
        ),
        migrations.AlterField(
            model_name='robotstatus',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 13, 8, 36, 124265)),
        ),
    ]
