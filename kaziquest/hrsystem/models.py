from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class Employee(models.Model):
class Employee(AbstractUser):
    id = models.AutoField(primary_key=True)
    EmployeeId = models.CharField(max_length=255, null=True, unique=True)
    Name = models.CharField(max_length=255)
    DOB = models.DateField(null=True)
    PhoneNumber = models.CharField(max_length=255, null=True)
    IDnumber = models.IntegerField(null=True)
    KRAPIN = models.CharField(max_length=255, null=True)
    Role = models.CharField(max_length=255, null=True)
    Company = models.CharField(max_length=255, null=True)
    Email_verified = models.BooleanField(default=False)
    Verification_token = models.CharField(max_length=255 , editable=False)
    username = None

    USERNAME_FIELD = 'EmployeeId'
    REQUIRED_FIELDS = []

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email')
        ]

class Assets(models.Model):
    AssetId = models.CharField(max_length=255, primary_key=True)
    AssetName = models.CharField(max_length=255)
    EmpId = models.CharField(max_length=255 , null=True)
    Description = models.CharField(max_length=255)
    Assigned_status = models.BooleanField(default=False)

class LeaveDays(models.Model):
    id = models.AutoField(primary_key=True)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Description = models.CharField(max_length=255)
    EmpId = models.CharField(max_length=255)
    Status = models.CharField(max_length=255, default='pending')




