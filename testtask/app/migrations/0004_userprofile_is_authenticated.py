# Generated by Django 4.2.4 on 2023-08-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_userprofile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
    ]
