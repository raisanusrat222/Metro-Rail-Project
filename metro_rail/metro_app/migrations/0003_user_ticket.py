# Generated by Django 3.2.7 on 2021-12-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro_app', '0002_rename_schedule_schedule_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.CharField(max_length=200, null=True)),
                ('train_no', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('email_address', models.CharField(max_length=200, null=True)),
                ('phone_number', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
