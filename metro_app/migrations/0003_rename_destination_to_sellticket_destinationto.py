# Generated by Django 4.0 on 2022-01-01 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metro_app', '0002_rename_travel_date_sellticket_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellticket',
            old_name='destination_to',
            new_name='destinationto',
        ),
    ]