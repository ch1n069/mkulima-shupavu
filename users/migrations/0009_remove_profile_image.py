# Generated by Django 4.0.5 on 2022-06-29 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='image',
        ),
    ]