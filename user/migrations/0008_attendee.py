# Generated by Django 4.2.2 on 2023-07-15 05:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("organizer", "0016_alter_eventdetails_eventimage"),
        ("user", "0007_alter_cartitem_quantity"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attendee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("attendeName", models.CharField(max_length=50)),
                ("attendeEmail", models.EmailField(max_length=30)),
                ("attendeGender", models.CharField(max_length=10)),
                ("attendeAddress", models.CharField(max_length=50)),
                ("attendeContact", models.PositiveIntegerField()),
                ("attendeCountry", models.CharField(max_length=20)),
                ("attendeState", models.CharField(max_length=20)),
                ("attendeZIP", models.PositiveIntegerField()),
                (
                    "timeStamp",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(2023, 7, 15, 11, 4, 4, 170168),
                        null=True,
                    ),
                ),
                (
                    "cartitem",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user.cartitem",
                    ),
                ),
                (
                    "event",
                    models.ForeignKey(
                        default=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="organizer.eventdetails",
                    ),
                ),
            ],
        ),
    ]
