# Generated by Django 3.2 on 2021-04-17 18:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0004_auto_20210417_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='package',
            name='time_arrived',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 21, 20, 25, 252099)),
        ),
        migrations.AlterField(
            model_name='package',
            name='time_of_departure',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 17, 21, 20, 25, 252099)),
        ),
        migrations.AlterField(
            model_name='robotstatus',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 17, 21, 20, 25, 253100)),
        ),
        migrations.AlterField(
            model_name='package',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='controller.position'),
        ),
    ]
