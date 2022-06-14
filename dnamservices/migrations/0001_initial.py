# Generated by Django 4.0.3 on 2022-06-14 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=50)),
                ('client_location', models.CharField(max_length=50)),
                ('client_street', models.CharField(max_length=50)),
                ('client_email', models.EmailField(max_length=254)),
                ('client_website', models.CharField(blank=True, max_length=50, null=True)),
                ('delete', models.BooleanField(default=False, verbose_name='delete')),
            ],
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=50)),
                ('employee_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('employee_address', models.CharField(blank=True, max_length=50, null=True)),
                ('employee_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('in_image', models.FileField(blank=True, null=True, upload_to='Invoice_in', verbose_name='File')),
                ('invoice_type', models.CharField(max_length=50, verbose_name='Type')),
                ('delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('out_image', models.FileField(blank=True, null=True, upload_to='Invoice_out', verbose_name='File')),
                ('invoice_type', models.CharField(max_length=50, verbose_name='Type')),
                ('delete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/services')),
                ('detail', models.TextField()),
                ('fade', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=50)),
                ('site_title', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('suburb', models.CharField(blank=True, default='', max_length=50)),
                ('postcode', models.CharField(blank=True, default='', max_length=50)),
                ('site_contact', models.CharField(blank=True, default='', max_length=50)),
                ('site_attribute', models.CharField(blank=True, default='', max_length=100)),
                ('service', models.CharField(blank=True, default='', max_length=100)),
                ('clean_schedule', models.CharField(blank=True, default='', max_length=100)),
                ('clean_area', models.CharField(blank=True, default='', max_length=50)),
                ('clean_task_enable', models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No')], default='', max_length=10)),
                ('startdate', models.DateField(blank=True)),
                ('extra_detail', models.TextField(blank=True)),
                ('sunday', models.IntegerField(blank=True, default='0')),
                ('monday', models.IntegerField(blank=True, default='0')),
                ('tuesday', models.IntegerField(blank=True, default='0')),
                ('wednesday', models.IntegerField(blank=True, default='0')),
                ('thrusday', models.IntegerField(blank=True, default='0')),
                ('friday', models.IntegerField(blank=True, default='0')),
                ('saturday', models.IntegerField(blank=True, default='0')),
                ('enter', models.BooleanField(verbose_name='save')),
                ('remove', models.BooleanField(default=False, verbose_name='delete')),
                ('cleaner', models.ManyToManyField(blank=True, default='', to='dnamservices.employee')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnamservices.client')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('clent_name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='Testimonials')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrderTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workorder', models.CharField(max_length=50)),
                ('workorder_title', models.CharField(max_length=50)),
                ('pricing', models.IntegerField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=50, null=True)),
                ('completed_by', models.CharField(blank=True, max_length=50, null=True)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('extra_detail', models.TextField(blank=True, null=True)),
                ('show', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False)),
                ('assigned_to', models.ManyToManyField(blank=True, null=True, to='dnamservices.employee')),
                ('client_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dnamservices.client')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnamservices.sites')),
                ('workorder_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Superviser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superviser_name', models.CharField(max_length=50)),
                ('superviser_address', models.CharField(max_length=50)),
                ('delete', models.BooleanField(default=False)),
                ('superviser_user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dnamservices.superviser'),
        ),
        migrations.CreateModel(
            name='ComplaintTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workorder', models.CharField(max_length=50)),
                ('pricing', models.IntegerField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=50, null=True)),
                ('completed_by', models.CharField(blank=True, max_length=50, null=True)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('extra_detail', models.TextField(blank=True, null=True)),
                ('show', models.BooleanField(default=False)),
                ('delete', models.BooleanField(default=False)),
                ('assigned_to', models.ManyToManyField(blank=True, null=True, to='dnamservices.employee')),
                ('client_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dnamservices.client')),
                ('complaint_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnamservices.sites')),
            ],
        ),
    ]