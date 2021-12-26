# Generated by Django 3.2.7 on 2021-12-25 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro_app', '0003_user_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='premium_ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(default='', max_length=30)),
                ('Last_Name', models.CharField(default='', max_length=30)),
                ('User_Name', models.CharField(default='', max_length=30)),
                ('Phone_Number', models.CharField(default='', max_length=30)),
                ('NID', models.CharField(default='', max_length=30)),
                ('Package', models.CharField(default='', max_length=30)),
                ('Pay_With', models.CharField(max_length=30)),
                ('Card_Num', models.CharField(default='', max_length=30)),
                ('Card_Status', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
