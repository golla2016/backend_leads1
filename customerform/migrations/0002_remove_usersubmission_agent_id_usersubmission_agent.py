# Generated by Django 5.0.6 on 2025-03-14 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0001_initial'),
        ('customerform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersubmission',
            name='agent_id',
        ),
        migrations.AddField(
            model_name='usersubmission',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='submissions', to='agents.agent'),
        ),
    ]
