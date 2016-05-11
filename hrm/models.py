from django.db import models

CompanyStatusChoices = (
    (0, 'enabled'),
    (1, 'disabled'),
    (2, 'expired'),
)


class Company(models.Model):
    name = models.CharField('company name', max_length=128)
    code = models.CharField('company code', max_length=32)
    password = models.CharField('company password', max_length=32)
    fullname = models.CharField('company full name', max_length=128)
    address = models.CharField('company address', max_length=128)
    contact_name = models.CharField('company contact name', max_length=16)
    contact_mobile = models.CharField('company mobile name', max_length=16)
    contact_email = models.CharField('company email name', max_length=64)
    status = models.IntegerField('company status', choices=CompanyStatusChoices)

    class Meta:
        app_label = 'hrm'


class Plugin(models.Model):
    company = models.ForeignKey(Company)
    installed_time = models.DateTimeField('installation time', auto_created=True)
    name = models.CharField('plugin name', max_length=32)
    description = models.TextField('plugin description')
    icon = models.ImageField('plugin icon')
    unique_id = models.CharField('plugin unique id', max_length=32)

    class Meta:
        app_label = 'hrm'


class ServiceRecord(models.Model):
    company = models.ForeignKey(Company)
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')

    class Meta:
        app_label = 'hrm'


class Department(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField('dep name', max_length=16)
    head = models.ForeignKey('hrm.Employee', related_name='department_head')

    class Meta:
        app_label = 'hrm'


class Employee(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField('emp name', max_length=16)
    work_no = models.CharField('emp work no', max_length=16)
    avatar = models.ImageField('emp avatar')
    status = models.IntegerField('emp status')
    mobile = models.CharField('emp mobile', max_length=20)
    birthday = models.DateField('emp birthday')
    department = models.ForeignKey(Department, blank=True)

    class Meta:
        app_label = 'hrm'


CertTypeChoices = (
    (0, 'id'),
    (1, 'passport'),
    (2, 'other')
)


class EmployeeCert(models.Model):
    employee = models.ForeignKey(Employee)
    type = models.IntegerField(choices=CertTypeChoices)
    number = models.CharField(max_length=128)

    class Meta:
        app_label = 'hrm'
