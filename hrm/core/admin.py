from django.contrib import admin
from django import forms
from .models import (
    Company,
    InstalledPlugin,
    ServiceRecord,
    Department,
    Employee,
    EmployeeCert,
    Account
)


class CompanyAdminForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyAdmin(admin.ModelAdmin):
    form = CompanyAdminForm
    list_display = ['name', 'code', 'fullname', 'address', 'contact_name', 'contact_mobile',
                    'contact_email', 'created_at', 'updated_at', 'status']
    readonly_fields = ['name', 'code', 'fullname', 'address', 'contact_name', 'contact_mobile',
                       'contact_email', 'created_at', 'updated_at', 'status']


admin.site.register(Company, CompanyAdmin)


class InstalledPluginAdminForm(forms.ModelForm):
    class Meta:
        model = InstalledPlugin
        fields = '__all__'


class InstalledPluginAdmin(admin.ModelAdmin):
    form = InstalledPluginAdminForm
    list_display = ['installed_time', 'name', 'description', 'icon', 'plugin_id', 'status']
    readonly_fields = ['installed_time', 'name', 'description', 'icon', 'plugin_id', 'status']


admin.site.register(InstalledPlugin, InstalledPluginAdmin)


class ServiceRecordAdminForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        fields = '__all__'


class ServiceRecordAdmin(admin.ModelAdmin):
    form = ServiceRecordAdminForm
    list_display = ['start_time', 'end_time']
    readonly_fields = ['start_time', 'end_time']


admin.site.register(ServiceRecord, ServiceRecordAdmin)


class DepartmentAdminForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentAdmin(admin.ModelAdmin):
    form = DepartmentAdminForm
    list_display = ['name']
    readonly_fields = ['name']


admin.site.register(Department, DepartmentAdmin)


class EmployeeAdminForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeAdminForm
    list_display = ['name', 'work_no', 'avatar', 'status', 'mobile', 'birthday']
    readonly_fields = ['name', 'work_no', 'avatar', 'status', 'mobile', 'birthday']


admin.site.register(Employee, EmployeeAdmin)


class EmployeeCertAdminForm(forms.ModelForm):
    class Meta:
        model = EmployeeCert
        fields = '__all__'


class EmployeeCertAdmin(admin.ModelAdmin):
    form = EmployeeCertAdminForm
    list_display = ['type', 'number']
    readonly_fields = ['type', 'number']


admin.site.register(EmployeeCert, EmployeeCertAdmin)


class AccountAdminForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


class AccountAdmin(admin.ModelAdmin):
    form = AccountAdminForm
    list_display = ['code', 'work_no', 'password']
    readonly_fields = ['code', 'work_no', 'password']


admin.site.register(Account, AccountAdmin)
