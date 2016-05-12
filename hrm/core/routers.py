from django.conf.urls import patterns, url, include
from rest_framework import routers
from .api import (
    CompanyViewSet,
    InstalledPluginViewSet,
    ServiceRecordViewSet,
    DepartmentViewSet,
    EmployeeViewSet,
    EmployeeCertViewSet
)

router = routers.DefaultRouter()
router.register('company', CompanyViewSet)
router.register('installedplugin', InstalledPluginViewSet)
router.register('servicerecord', ServiceRecordViewSet)
router.register('department', DepartmentViewSet)
router.register('employee', EmployeeViewSet)
router.register('employeecert', EmployeeCertViewSet)

