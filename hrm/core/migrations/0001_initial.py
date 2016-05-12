# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_created=True, verbose_name='creation time')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('code', models.CharField(max_length=32, verbose_name='code')),
                ('password', models.CharField(max_length=32, verbose_name='password')),
                ('fullname', models.CharField(max_length=128, verbose_name='full name')),
                ('address', models.CharField(max_length=128, verbose_name='address')),
                ('contact_name', models.CharField(max_length=16, verbose_name='contact name')),
                ('contact_mobile', models.CharField(max_length=16, verbose_name='contact mobile')),
                ('contact_email', models.CharField(max_length=64, verbose_name='contact email')),
                ('status', models.IntegerField(choices=[(0, 'enabled'), (1, 'disabled'), (2, 'expired')], verbose_name='status')),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'verbose_name': 'company',
                'ordering': ['creation_time', '-status'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='dep name')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Company')),
            ],
            options={
                'verbose_name_plural': 'departments',
                'verbose_name': 'department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='emp name')),
                ('work_no', models.CharField(max_length=16, verbose_name='emp work no')),
                ('avatar', models.ImageField(upload_to='', verbose_name='emp avatar')),
                ('status', models.IntegerField(verbose_name='emp status')),
                ('mobile', models.CharField(max_length=20, verbose_name='emp mobile')),
                ('birthday', models.DateField(verbose_name='emp birthday')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Company')),
                ('department', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.Department')),
            ],
            options={
                'verbose_name_plural': 'employees',
                'verbose_name': 'employee',
            },
        ),
        migrations.CreateModel(
            name='EmployeeCert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'id'), (1, 'passport'), (2, 'other')])),
                ('number', models.CharField(max_length=128)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Employee')),
            ],
            options={
                'verbose_name_plural': 'employee certificates',
                'verbose_name': 'employee certificate',
            },
        ),
        migrations.CreateModel(
            name='InstalledPlugin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installed_time', models.DateTimeField(auto_created=True, verbose_name='installation time')),
                ('name', models.CharField(max_length=32, verbose_name='plugin name')),
                ('description', models.TextField(verbose_name='plugin description')),
                ('icon', models.ImageField(upload_to='', verbose_name='plugin icon')),
                ('plugin_id', models.CharField(max_length=32, verbose_name='plugin id')),
                ('status', models.IntegerField(choices=[(0, 'installed'), (1, 'disabled'), (1, 'uninstalled')], verbose_name='plugin status')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Company')),
            ],
            options={
                'verbose_name_plural': 'installed plugins',
                'verbose_name': 'installed plugin',
                'ordering': ['installed_time', 'status'],
            },
        ),
        migrations.CreateModel(
            name='ServiceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='start time')),
                ('end_time', models.DateTimeField(verbose_name='end time')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Company')),
            ],
            options={
                'verbose_name_plural': 'service records',
                'verbose_name': 'service record',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_head', to='core.Employee'),
        ),
        migrations.AddField(
            model_name='department',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Department'),
        ),
    ]
