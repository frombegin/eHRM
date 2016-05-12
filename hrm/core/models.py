from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password


# abstract models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField('creation time', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('update time', auto_now=True, editable=False)

    class Meta:
        abstract = True


class TimeFramedModel(models.Model):
    start_at = models.DateTimeField('start time', null=True, blank=True)
    end_at = models.DateTimeField('end time', null=True, blank=True)

    class Meta:
        abstract = True


# core models

CompanyStatusChoices = (
    (0, 'enabled'),
    (1, 'disabled'),
    (2, 'expired'),
)


class Company(TimeStampedModel):
    name = models.CharField('name', max_length=128)
    code = models.CharField('code', max_length=32)
    fullname = models.CharField('full name', max_length=128)
    address = models.CharField('address', max_length=128)
    contact_name = models.CharField('contact name', max_length=16)
    contact_mobile = models.CharField('contact mobile', max_length=16)
    contact_email = models.CharField('contact email', max_length=64)
    status = models.IntegerField('status', choices=CompanyStatusChoices)

    class Meta:
        verbose_name = "company"
        verbose_name_plural = "Companies"
        ordering = ['updated_at', '-status']

    def __str__(self):
        return self.name


InstalledPluginStatusChoices = (
    (0, 'installed'),
    (1, 'disabled'),
    (1, 'uninstalled'),
)


class InstalledPlugin(models.Model):
    company = models.ForeignKey('Company')
    installed_time = models.DateTimeField('installation time', auto_created=True)
    name = models.CharField('plugin name', max_length=32)
    description = models.TextField('plugin description')
    icon = models.ImageField('plugin icon')
    plugin_id = models.CharField('plugin id', max_length=32)
    status = models.IntegerField('plugin status', choices=InstalledPluginStatusChoices)

    class Meta:
        verbose_name = "installed plugin"
        verbose_name_plural = "installed plugins"
        ordering = ['installed_time', 'status']


class ServiceRecord(models.Model):
    company = models.ForeignKey(Company)
    start_time = models.DateTimeField('start time')
    end_time = models.DateTimeField('end time')

    class Meta:
        verbose_name = "service record"
        verbose_name_plural = "service records"


class Department(models.Model):
    company = models.ForeignKey(Company)
    name = models.CharField('dep name', max_length=16)
    head = models.ForeignKey('Employee', related_name='department_head')
    parent = models.ForeignKey('self')

    class Meta:
        verbose_name = "department"
        verbose_name_plural = "departments"


class EmployeeStatus(object):
    JOINED = 0
    LEAVED = 1
    INACTIVE = 2

    CHOICES = (
        (JOINED, 'JOINED'),
        (LEAVED, 'LEAVED'),
        (INACTIVE, 'INACTIVE'),
    )

    @classmethod
    def choices(cls): return cls.CHOICES

    @classmethod
    def get_display_text(cls, status):
        return cls.CHOICES[status]


class Employee(models.Model):
    company = models.ForeignKey('Company')
    name = models.CharField('name', max_length=16)
    work_no = models.CharField('work no', max_length=16)
    avatar = models.ImageField('avatar', null=True)
    status = models.IntegerField('status', choices=EmployeeStatus.choices(), default=EmployeeStatus.JOINED)
    mobile = models.CharField('mobile', max_length=20)
    birthday = models.DateField('birthday')
    department = models.ForeignKey('Department', blank=True, null=True)

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"

    def __str__(self):
        return self.name


class Account(models.Model):
    code = models.CharField('company code', max_length=32)
    work_no = models.CharField('work no', max_length=16)
    password = models.CharField('password', max_length=32)

    class Meta:
        verbose_name = "account"
        verbose_name_plural = "accounts"


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
        verbose_name = "employee certificate"
        verbose_name_plural = "employee certificates"


@receiver(signal=signals.post_save, sender=Company, dispatch_uid="add_account")
def add_account(sender, instance, **kwargs):
    Account.objects.create(code=instance.code,
                           work_no='',  # '' means company supervisor
                           password=make_password('123456'))


@receiver(signal=signals.post_delete, sender=Company, dispatch_uid="del_account")
def del_account(sender, instance, **kwargs):
    Account.objects.filter(code=instance.code).delete()


@receiver(signal=signals.post_save, sender=Employee, dispatch_uid="add_sub_account")
def add_sub_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(code=instance.company.code,
                               work_no=instance.work_no,
                               password=make_password('123456'))


@receiver(signal=signals.post_delete, sender=Employee, dispatch_uid="del_sub_account")
def del_sub_account(sender, instance, **kwargs):
    Account.objects.filter(code=instance.company.code,
                           work_no=instance.work_no).delete()
