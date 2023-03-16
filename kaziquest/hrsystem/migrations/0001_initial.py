# Generated by Django 4.1.7 on 2023-03-16 09:10

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('AssetId', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('AssetName', models.CharField(max_length=255)),
                ('EmpId', models.CharField(max_length=255, null=True)),
                ('Description', models.CharField(max_length=255)),
                ('Assigned_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveDays',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Description', models.CharField(max_length=255)),
                ('EmpId', models.CharField(max_length=255)),
                ('Status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('EmployeeId', models.CharField(max_length=255, null=True, unique=True)),
                ('Name', models.CharField(max_length=255)),
                ('DOB', models.DateField(null=True)),
                ('PhoneNumber', models.CharField(max_length=255, null=True)),
                ('IDnumber', models.IntegerField(null=True)),
                ('KRAPIN', models.CharField(max_length=255, null=True)),
                ('Role', models.CharField(max_length=255, null=True)),
                ('Company', models.CharField(max_length=255, null=True)),
                ('Email_verified', models.BooleanField(default=False)),
                ('Verification_token', models.CharField(editable=False, max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='employee',
            constraint=models.UniqueConstraint(fields=('email',), name='unique_email'),
        ),
    ]
