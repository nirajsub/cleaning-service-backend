# Generated by Django 4.0.3 on 2022-06-14 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dnamservices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='delete',
        ),
    ]
