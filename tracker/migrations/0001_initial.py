# Generated by Django 5.0.6 on 2024-06-15 21:28

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Customer Details',
            },
        ),
        migrations.CreateModel(
            name='TractorBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Tractor Brands',
            },
        ),
        migrations.CreateModel(
            name='Implement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('chassis_number', models.CharField(max_length=100, unique=True)),
                ('color', models.CharField(max_length=50)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='implements_owned', to='tracker.customer')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='implements_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Implement Details',
            },
        ),
        migrations.CreateModel(
            name='TractorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=100, unique=True)),
                ('chassis_number', models.CharField(max_length=100, unique=True)),
                ('engine_number', models.CharField(max_length=100, unique=True)),
                ('color', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.tractorbrand')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tractors_owned', to='tracker.customer')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tractors_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Tractor Details',
            },
        ),
        migrations.CreateModel(
            name='OwnershipHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True)),
                ('implement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.implement')),
                ('new_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='new_ownerships', to='tracker.customer')),
                ('previous_owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous_ownerships', to='tracker.customer')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tractor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.tractordetails')),
            ],
            options={
                'db_table': 'Ownership History',
            },
        ),
        migrations.CreateModel(
            name='TractorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.tractorbrand')),
            ],
            options={
                'db_table': 'Tractor Models',
            },
        ),
        migrations.AddField(
            model_name='tractordetails',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.tractormodel'),
        ),
    ]
