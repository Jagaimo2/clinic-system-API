from rest_framework import serializers
from .models import ClinicUser, Clinic, Staff, Message, Appointment

class ClinicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicUser
        fields = ['id', 'first_name', 'middle_name', 'last_name', 'email', 'address', 'contact', 'sex']

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'name', 'address', 'contact', 'email', 'operation_start', 'operation_end',
                  'starting_day', 'end_day', 'description']

class StaffSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    role = serializers.StringRelatedField()
    specialization = serializers.StringRelatedField(many=True)

    class Meta:
        model = Staff
        fields = ['id', 'user', 'role', 'specialization']

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = ['content', 'date', 'sender', 'recipient']

class AppointmentSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField()
    clinic = serializers.StringRelatedField()

    class Meta:
        model = Appointment
        fields = ['id', 'appointment_date', 'appointment_status', 'category', 'doctor', 'clinic']
