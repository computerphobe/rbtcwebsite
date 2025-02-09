# Generated by Django 4.2.16 on 2024-11-21 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbtcwebapp', '0030_remove_profile_bio_remove_profile_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedcomponent',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 21, 12, 54, 14, 910993, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=100),
        ),
    ]
