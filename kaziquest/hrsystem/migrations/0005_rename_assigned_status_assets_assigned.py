# Generated by Django 4.1.7 on 2023-03-16 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrsystem', '0004_alter_leavedays_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assets',
            old_name='Assigned_status',
            new_name='Assigned',
        ),
    ]
