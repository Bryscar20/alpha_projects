# Generated by Django 5.0.6 on 2024-06-15 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('live_tracking_data', '0004_live_tracking_data_iccid1_live_tracking_data_iccid2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='live_tracking_data',
            name='iccid1',
        ),
        migrations.RemoveField(
            model_name='live_tracking_data',
            name='iccid2',
        ),
    ]
