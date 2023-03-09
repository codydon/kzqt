from rest_framework import serializers
from .models import Employee, Assets, LeaveDays

# class NoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Note
#         fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveDays
        fields = '__all__'