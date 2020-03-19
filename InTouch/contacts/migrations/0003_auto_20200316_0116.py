# Generated by Django 3.0.4 on 2020-03-15 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20200315_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='business_address',
        ),
        migrations.AddField(
            model_name='contact',
            name='img_src',
            field=models.CharField(default=None, max_length=200, verbose_name='Business Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(default=None, max_length=25, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='home_address',
            field=models.CharField(default=None, max_length=200, verbose_name='Home Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='job_title',
            field=models.CharField(default=None, max_length=20, verbose_name='Job Title'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default=None, max_length=30, verbose_name='Last Name'),
        ),
    ]
