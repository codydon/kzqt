from rest_framework import serializers
from .models import Employee, Assets, LeaveDays, Notification


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

        # fiels being used
        # fields = ['EmployeeId', 'Name', 'DOB', 'PhoneNumber', 'IDnumber', 'KRAPIN', 'Role', 'Company', 'Email_verified', 'Verification_token', 'email', 'password']
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }
    
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

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        # fields = ('id', 'EmpId', 'message', 'timestamp')
        fields = '__all__'