from rest_framework import serializers
from .models import Staff


class myStaffs(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = [
            'name',
            'age',
            'role',
            'staff_number'
        ]