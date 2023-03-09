from django.db import models
import uuid
# Create your models here.
class Employee(models.Model):
    EmployeeId = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    DOB = models.DateField(null=True)
    PhoneNumber = models.IntegerField(null=True)
    IDnumber = models.IntegerField(null=True)
    KRAPIN = models.CharField(max_length=255, null=True)
    Email = models.EmailField()
    Role = models.CharField(max_length=255, null=True)
    Password = models.CharField(max_length=255, null=True)
  


class LeaveDays(models.Model):
    EmployeeId = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Description = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)

class Assets(models.Model):
    EmployeeId = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    AssetName = models.CharField(max_length=255)
    AssetId = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)

class AssetTrack(models.Model):
    AssetId = models.OneToOneField(Assets, on_delete=models.CASCADE, primary_key=True)
    DateIssued = models.DateField()
    ConditionIssued = models.CharField(max_length=255)
    IssuedDesc = models.CharField(max_length=255)
    DateReturned = models.DateField(null=True, blank=True)
    ConditionReturned = models.CharField(max_length=255, null=True, blank=True)
    ReturnedDesc = models.CharField(max_length=255, null=True, blank=True)


