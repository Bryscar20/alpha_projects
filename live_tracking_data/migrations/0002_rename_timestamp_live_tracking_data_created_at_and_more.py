# Generated by Django 5.0.6 on 2024-06-14 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_tracking_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='live_tracking_data',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='live_tracking_data',
            old_name='raw_data',
            new_name='other_data',
        ),
        migrations.AddField(
            model_name='live_tracking_data',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='live_tracking_data',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='live_tracking_data',
            name='speed',
            field=models.FloatField(default=0.0),
        ),
    ]