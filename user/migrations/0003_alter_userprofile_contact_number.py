# Generated by Django 4.2.2 on 2023-07-11 02:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_userprofile_user_about_userprofile_user_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="contact_number",
            field=models.CharField(default=True, max_length=15),
        ),
    ]