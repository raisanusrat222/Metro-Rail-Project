# Generated by Django 4.0 on 2021-12-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro_app', '0002_delete_schedule_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(default='', max_length=30)),
                ('Last_Name', models.CharField(default='', max_length=30)),
                ('User_Name', models.CharField(default='', max_length=30)),
                ('Phone_Number', models.CharField(default='', max_length=30)),
                ('NID', models.CharField(default='', max_length=30)),
                ('Address', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
