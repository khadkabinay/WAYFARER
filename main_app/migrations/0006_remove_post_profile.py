# Generated by Django 3.1.2 on 2020-10-09 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_profile_join_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profile',
        ),
    ]