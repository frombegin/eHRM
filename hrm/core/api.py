from rest_framework import viewsets, permissions
from .models import (
    Company,
    InstalledPlugin,
    ServiceRecord,
    Department,
    Employee,
    EmployeeCert
)
from .serializers import (
    CompanySerializer,
    InstalledPluginSerializer,
    ServiceRecordSerializer,
    DepartmentSerializer,
    EmployeeSerializer,
    EmployeeCertSerializer
)


class CompanyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Company class"""

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class InstalledPluginViewSet(viewsets.ModelViewSet):
    """ViewSet for the InstalledPlugin class"""

    queryset = InstalledPlugin.objects.all()
    serializer_class = InstalledPluginSerializer
    permission_classes = [permissions.IsAuthenticated]


class ServiceRecordViewSet(viewsets.ModelViewSet):
    """ViewSet for the ServiceRecord class"""

    queryset = ServiceRecord.objects.all()
    serializer_class = ServiceRecordSerializer
    permission_classes = [permissions.IsAuthenticated]


class DepartmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Department class"""

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(viewsets.ModelViewSet):
    """ViewSet for the Employee class"""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeCertViewSet(viewsets.ModelViewSet):
    """ViewSet for the EmployeeCert class"""

    queryset = EmployeeCert.objects.all()
    serializer_class = EmployeeCertSerializer
    permission_classes = [permissions.IsAuthenticated]
