# Generated by Django 4.0.5 on 2022-06-29 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_name_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]