# Generated by Django 3.2 on 2022-08-11 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnamservices', '0008_auto_20220810_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/career')),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ourteam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/team')),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactUs',
        ),
    ]
