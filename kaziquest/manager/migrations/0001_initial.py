# Generated by Django 4.1.7 on 2023-03-09 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('DOB', models.DateField(null=True)),
                ('PhoneNumber', models.IntegerField(null=True)),
                ('IDnumber', models.IntegerField(null=True)),
                ('KRAPIN', models.CharField(max_length=255, null=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Role', models.CharField(max_length=255, null=True)),
                ('Password', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('EmployeeId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='manager.employee')),
                ('AssetName', models.CharField(max_length=255)),
                ('AssetId', models.CharField(max_length=255)),
                ('Description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveDays',
            fields=[
                ('EmployeeId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='manager.employee')),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Description', models.CharField(max_length=255)),
                ('Status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AssetTrack',
            fields=[
                ('AssetId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='manager.assets')),
                ('DateIssued', models.DateField()),
                ('ConditionIssued', models.CharField(max_length=255)),
                ('IssuedDesc', models.CharField(max_length=255)),
                ('DateReturned', models.DateField(blank=True, null=True)),
                ('ConditionReturned', models.CharField(blank=True, max_length=255, null=True)),
                ('ReturnedDesc', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
