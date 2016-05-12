from rest_framework import serializers
from .models import (
    Company,
    InstalledPlugin,
    ServiceRecord,
    Department,
    Employee,
    EmployeeCert
)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'code',
            'fullname',
            'address',
            'contact_name',
            'contact_mobile',
            'contact_email',
            'created_at',
            'updated_at',
            'status',
        )


class InstalledPluginSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstalledPlugin
        fields = (
            'id',
            'installed_time',
            'name',
            'description',
            'icon',
            'plugin_id',
            'status',
        )


class ServiceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRecord
        fields = (
            'id',
            'start_time',
            'end_time',
        )


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id',
            'name',
        )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'work_no',
            'avatar',
            'status',
            'mobile',
            'birthday',
            'company'
        )


class EmployeeCertSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCert
        fields = (
            'id',
            'type',
            'number',
        )
