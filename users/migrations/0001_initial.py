# Generated by Django 4.0.5 on 2022-07-13 08:53

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(default='', max_length=255)),
                ('last_name', models.CharField(default='', max_length=255)),
                ('username', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField(default=0)),
                ('location', models.CharField(default='place', max_length=255)),
                ('role', models.CharField(choices=[(1, 'farmer'), (2, 'buyer'), (4, 'supplier'), (3, 'agent'), (5, 'admin')], max_length=20)),
                ('password', models.CharField(max_length=255)),
                ('confirm_password', models.CharField(max_length=255)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Guarantor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('contact', models.IntegerField(default=0)),
                ('location', models.CharField(default='', max_length=255)),
                ('identification_number', models.IntegerField()),
                ('identification_card', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Inputs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fertilizer_name', models.CharField(default='fertilizer', max_length=255)),
                ('chemical_name', models.CharField(default='pesticide', max_length=255)),
                ('seed_name', models.CharField(default='certified seed', max_length=255)),
                ('fertilizer_bags', models.IntegerField(null=True)),
                ('seed_bags', models.IntegerField(null=True)),
                ('chemicals', models.IntegerField(null=True)),
                ('fertilizer_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('seed_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('chemicals_price', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputs_total', models.IntegerField(null=True)),
                ('invoice', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('user_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.inputs')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('contact', models.BigIntegerField(default=0)),
                ('location', models.CharField(default='', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identification_number', models.IntegerField()),
                ('mpesa_statements', models.ImageField(upload_to='images/')),
                ('identification_card', models.ImageField(upload_to='images/')),
                ('loan_amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('production', models.IntegerField(null=True)),
                ('land_size', models.DecimalField(decimal_places=2, max_digits=20)),
                ('revenue', models.DecimalField(decimal_places=2, max_digits=20)),
                ('amount_payable', models.DecimalField(decimal_places=2, max_digits=20)),
                ('crop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.crop')),
                ('guarantor', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.guarantor')),
                ('inputs_picked', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.inputs')),
                ('user_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop_to_buy', models.CharField(max_length=255)),
                ('bags_to_buy', models.IntegerField(null=True)),
                ('invoice', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=20)),
                ('user_details', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
