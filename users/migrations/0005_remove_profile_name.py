# Generated by Django 4.0.5 on 2022-06-29 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_land_output'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
