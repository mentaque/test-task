# Generated by Django 4.2.4 on 2023-08-17 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('auth_code', models.CharField(default='0000', max_length=4)),
                ('invite_code', models.CharField(blank=True, max_length=6, null=True)),
                ('invited_users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userprofile')),
            ],
        ),
    ]