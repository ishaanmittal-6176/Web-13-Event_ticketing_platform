# Generated by Django 4.2.2 on 2023-07-24 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0017_attendee_secreatecode_alter_attendee_timestamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendee",
            name="secreateCode",
            field=models.CharField(default=True, max_length=200),
        ),
        migrations.AlterField(
            model_name="attendee",
            name="timeStamp",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2023, 7, 24, 16, 27, 42, 242242),
                null=True,
            ),
        ),
    ]