# Generated by Django 2.2.6 on 2020-11-27 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GEN', '0013_userprofileinfo_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='app_user_name',
            field=models.CharField(default='NONE', max_length=40),
        ),
    ]
