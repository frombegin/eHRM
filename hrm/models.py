from django.db import models


# abstract models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField('creation time', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('update time', auto_now=True, editable=False)

    class Meta:
        abstract = True


class TimeFramedModel(models.Model):
    start_at = models.DateTimeField('start time', null=True, blank=True)
    end = models.DateTimeField('end time', null=True, blank=True)

    class Meta:
        abstract = True


# core models

CompanyStatusChoices = (
    (0, 'enabled'),
    (1, 'disabled'),
    (2, 'expired'),
)


class Company(models.Model):
    name = models.CharField('name', max_length=128)
    code = models.CharField('code', max_length=32)
    password = models.CharField('password', max_length=32)
    fullname = models.CharField('full name', max_length=128)
    address = models.CharField('address', max_length=128)
    contact_name = models.CharField('contact name', max_length=16)
    contact_mobile = models.CharField('contact mobile', max_length=16)
    contact_email = models.CharField('contact email', max_length=64)
    creation_time = models.DateTimeField('creation time', auto_created=True)
    status = models.IntegerField('status', choices=CompanyStatusChoices)

    class Meta:
        app_label = 'hrm'
        ordering = ['creation_time', '-status']


InstalledPluginStatusChoices = (
    (0, 'installed'),
    (1, 'disabled'),
    (1, 'uninstalled'),
)


class InstalledPlugin(models.Model):
    company = models.ForeignKey(Company)
    installed_time = models.DateTimeField('installation time', auto_created=True)
    name = models.CharField('plugin name', max_length=32)
    description = models.TextField('plugin description')
    icon = models.ImageField('plugin icon')
    plugin_id = models.CharField('plugin id', max_length=32)
    status = models.IntegerField('plugin status', choices=InstalledPluginStatusChoices)

    class Meta:
        app_label = 'hrm'
        ordering = ['installed_time', 'status']


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
    parent = models.ForeignKey('self')

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
