# Generated by Django 3.2 on 2021-04-17 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0002_auto_20210417_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='RobotStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(default=datetime.datetime(2021, 4, 17, 20, 30, 58, 99207))),
                ('status', models.CharField(choices=[('A', 'Await package'), ('M', 'Moving'), ('IS', 'In stock')], default='A', max_length=4)),
            ],
        ),
        migrations.AlterField(
            model_name='package',
            name='time_arrived',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 20, 30, 58, 99207)),
        ),
        migrations.AlterField(
            model_name='package',
            name='time_of_departure',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 17, 20, 30, 58, 99207)),
        ),
    ]
