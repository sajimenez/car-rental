# Generated by Django 3.0.6 on 2020-05-05 15:49

import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this object should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this object should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'cars',
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this object should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('doors', models.IntegerField(choices=[(2, 'Two'), (4, 'Four'), (5, 'Five')], verbose_name='doors')),
                ('is_diesel', models.BooleanField(default=False, verbose_name='is diesel')),
                ('size', models.CharField(choices=[('minicompact', 'Minicompact'), ('compact', 'Compact'), ('van', 'Van'), ('pickup', 'Pick up')], max_length=64, verbose_name='size')),
            ],
            options={
                'verbose_name': 'car model',
                'verbose_name_plural': 'car models',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this object should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_from', models.DateTimeField(verbose_name='date from')),
                ('date_until', models.DateTimeField(verbose_name='date until')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='core.Car', verbose_name='car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='core.User', verbose_name='user')),
            ],
            options={
                'verbose_name': 'reservation',
                'verbose_name_plural': 'reservations',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='car_model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='core.CarModel', verbose_name='car model'),
        ),
    ]
