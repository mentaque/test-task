# Generated by Django 4.2.4 on 2023-08-17 12:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_invited_users_userprofile_inviter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone number must start with 7 and have a total length of 11 characters.', regex='^7\\d{10}$')]),
        ),
    ]
