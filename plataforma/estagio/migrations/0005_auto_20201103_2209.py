# Generated by Django 2.2.13 on 2020-11-04 01:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0004_auto_20200827_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conveniomodel',
            name='data_validade',
            field=models.DateTimeField(default=datetime.datetime(2025, 11, 4, 1, 9, 44, 190868, tzinfo=utc)),
        ),
    ]
