from django.db import models

# class Note(models.Model):
#     content = models.TextField()

class Employee(models.Model):
    EmployeeId = models.CharField(max_length=255, primary_key=True)
    Name = models.CharField(max_length=255)
    DOB = models.DateField(null=True)
    PhoneNumber = models.IntegerField(null=True)
    IDnumber = models.IntegerField(null=True)
    KRAPIN = models.CharField(max_length=255, null=True)
    Email = models.EmailField()
    Role = models.CharField(max_length=255, null=True)
    Password = models.CharField(max_length=255, null=True)
    Email_verified = models.BooleanField(default=False)
    Verification_token = models.CharField(max_length=255 , editable=False)

class Assets(models.Model):
    EmployeeId = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    AssetName = models.CharField(max_length=255)
    AssetId = models.CharField(max_length=255)
    Description = models.CharField(max_length=255)
    Assigned_status = models.BooleanField(default=False)

class LeaveDays(models.Model):
    EmployeeId = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Description = models.CharField(max_length=255)
    Status = models.CharField(max_length=255)


