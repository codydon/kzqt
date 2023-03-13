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
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveDays
        fields = '__all__'