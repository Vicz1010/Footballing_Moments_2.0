# Generated by Django 3.2.8 on 2021-10-21 15:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_alter_comment_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 21, 15, 44, 55, 615230, tzinfo=utc)),
        ),
    ]
