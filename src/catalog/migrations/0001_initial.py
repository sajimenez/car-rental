# Generated by Django 3.0.5 on 2020-04-30 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('doors', models.IntegerField(choices=[(2, 'Two'), (4, 'Four'), (5, 'Five')])),
                ('is_diesel', models.BooleanField(default=False)),
                ('size', models.CharField(choices=[('minicompact', 'Minicompact'), ('compact', 'Compact'), ('van', 'Van'), ('pickup', 'Pickup')], max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='catalog.CarModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]