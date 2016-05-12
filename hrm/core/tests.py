import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from django.contrib.auth.models import User, Group
from django.contrib.contenttypes.models import ContentType
from .models import (
    Company,
    InstalledPlugin,
    ServiceRecord,
    Department,
    Employee,
    EmployeeCert
)


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_company(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["code"] = "code"
    defaults["password"] = "password"
    defaults["fullname"] = "fullname"
    defaults["address"] = "address"
    defaults["contact_name"] = "contact_name"
    defaults["contact_mobile"] = "contact_mobile"
    defaults["contact_email"] = "contact_email"
    defaults["creation_time"] = "creation_time"
    defaults["status"] = "status"
    defaults.update(**kwargs)
    return Company.objects.create(**defaults)


def create_installedplugin(**kwargs):
    defaults = {}
    defaults["installed_time"] = "installed_time"
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults["icon"] = "icon"
    defaults["plugin_id"] = "plugin_id"
    defaults["status"] = "status"
    defaults.update(**kwargs)
    if "company" not in defaults:
        defaults["company"] = create_company()
    return InstalledPlugin.objects.create(**defaults)


def create_servicerecord(**kwargs):
    defaults = {}
    defaults["start_time"] = "start_time"
    defaults["end_time"] = "end_time"
    defaults.update(**kwargs)
    if "company" not in defaults:
        defaults["company"] = create_company()
    return ServiceRecord.objects.create(**defaults)


def create_department(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    if "company" not in defaults:
        defaults["company"] = create_company()
    if "head" not in defaults:
        defaults["head"] = create_employee()
    # if "parent" not in defaults:
    #     defaults["parent"] = create_department()
    return Department.objects.create(**defaults)


def create_employee(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["work_no"] = "work_no"
    defaults["avatar"] = "avatar"
    defaults["status"] = "status"
    defaults["mobile"] = "mobile"
    defaults["birthday"] = "birthday"
    defaults.update(**kwargs)
    if "company" not in defaults:
        defaults["company"] = create_company()
    if "department" not in defaults:
        defaults["department"] = create_department()
    return Employee.objects.create(**defaults)


def create_employeecert(**kwargs):
    defaults = {}
    defaults["type"] = "type"
    defaults["number"] = "number"
    defaults.update(**kwargs)
    if "employee" not in defaults:
        defaults["employee"] = create_employee()
    return EmployeeCert.objects.create(**defaults)


class CompanyViewTest(unittest.TestCase):
    '''
    Tests for Company
    '''

    def setUp(self):
        self.client = Client()

    def test_list_company(self):
        url = reverse('app_name_company_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_company(self):
        url = reverse('app_name_company_create')
        data = {
            "name": "name",
            "code": "code",
            "password": "password",
            "fullname": "fullname",
            "address": "address",
            "contact_name": "contact_name",
            "contact_mobile": "contact_mobile",
            "contact_email": "contact_email",
            "creation_time": "creation_time",
            "status": "status",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_company(self):
        company = create_company()
        url = reverse('app_name_company_detail', args=[company.id, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_company(self):
        company = create_company()
        data = {
            "name": "name",
            "code": "code",
            "password": "password",
            "fullname": "fullname",
            "address": "address",
            "contact_name": "contact_name",
            "contact_mobile": "contact_mobile",
            "contact_email": "contact_email",
            "creation_time": "creation_time",
            "status": "status",
        }
        url = reverse('app_name_company_update', args=[company.id, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class InstalledPluginViewTest(unittest.TestCase):
    '''
    Tests for InstalledPlugin
    '''

    def setUp(self):
        self.client = Client()

    def test_list_installedplugin(self):
        url = reverse('app_name_installedplugin_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_installedplugin(self):
        url = reverse('app_name_installedplugin_create')
        data = {
            "installed_time": "installed_time",
            "name": "name",
            "description": "description",
            "icon": "icon",
            "plugin_id": "plugin_id",
            "status": "status",
            "company": create_company().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_installedplugin(self):
        installedplugin = create_installedplugin()
        url = reverse('app_name_installedplugin_detail', args=[installedplugin.id, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_installedplugin(self):
        installedplugin = create_installedplugin()
        data = {
            "installed_time": "installed_time",
            "name": "name",
            "description": "description",
            "icon": "icon",
            "plugin_id": "plugin_id",
            "status": "status",
            "company": create_company().id,
        }
        url = reverse('app_name_installedplugin_update', args=[installedplugin.id, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ServiceRecordViewTest(unittest.TestCase):
    '''
    Tests for ServiceRecord
    '''

    def setUp(self):
        self.client = Client()

    def test_list_servicerecord(self):
        url = reverse('app_name_servicerecord_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_servicerecord(self):
        url = reverse('app_name_servicerecord_create')
        data = {
            "start_time": "start_time",
            "end_time": "end_time",
            "company": create_company().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_servicerecord(self):
        servicerecord = create_servicerecord()
        url = reverse('app_name_servicerecord_detail', args=[servicerecord.id, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_servicerecord(self):
        servicerecord = create_servicerecord()
        data = {
            "start_time": "start_time",
            "end_time": "end_time",
            "company": create_company().id,
        }
        url = reverse('app_name_servicerecord_update', args=[servicerecord.id, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DepartmentViewTest(unittest.TestCase):
    '''
    Tests for Department
    '''

    def setUp(self):
        self.client = Client()

    def test_list_department(self):
        url = reverse('app_name_department_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_department(self):
        url = reverse('app_name_department_create')
        data = {
            "name": "name",
            "company": create_company().id,
            "head": create_employee().id,
            # "parent": create_        'self'().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_department(self):
        department = create_department()
        url = reverse('app_name_department_detail', args=[department.id, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_department(self):
        department = create_department()
        data = {
            "name": "name",
            "company": create_company().id,
            "head": create_employee().id,
            # "parent": create_        'self'().id,
        }
        url = reverse('app_name_department_update', args=[department.id, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class EmployeeViewTest(unittest.TestCase):
    '''
    Tests for Employee
    '''

    def setUp(self):
        self.client = Client()

    def test_list_employee(self):
        url = reverse('app_name_employee_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_employee(self):
        url = reverse('app_name_employee_create')
        data = {
            "name": "name",
            "work_no": "work_no",
            "avatar": "avatar",
            "status": "status",
            "mobile": "mobile",
            "birthday": "birthday",
            "company": create_company().id,
            "department": create_department().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_employee(self):
        employee = create_employee()
        url = reverse('app_name_employee_detail', args=[employee.id, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_employee(self):
        employee = create_employee()
        data = {
            "name": "name",
            "work_no": "work_no",
            "avatar": "avatar",
            "status": "status",
            "mobile": "mobile",
            "birthday": "birthday",
            "company": create_company().id,
            "department": create_department().id,
        }
        url = reverse('app_name_employee_update', args=[employee.id, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class EmployeeCertViewTest(unittest.TestCase):
    '''
    Tests for EmployeeCert
    '''

    def setUp(self):
        self.client = Client()

    def test_list_employeecert(self):
        url = reverse('app_name_employeecert_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_employeecert(self):
        url = reverse('app_name_employeecert_create')
        data = {
            "type": "type",
            "number": "number",
            "employee": create_employee().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_employeecert(self):
        employeecert = create_employeecert()
        url = reverse('app_name_employeecert_detail', args=[employeecert.id, ])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_employeecert(self):
        employeecert = create_employeecert()
        data = {
            "type": "type",
            "number": "number",
            "employee": create_employee().id,
        }
        url = reverse('app_name_employeecert_update', args=[employeecert.id, ])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
