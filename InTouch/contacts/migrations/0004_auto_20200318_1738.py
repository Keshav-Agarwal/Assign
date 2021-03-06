# Generated by Django 3.0.4 on 2020-03-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20200316_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=25, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, verbose_name='E-mail Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='home_address',
            field=models.CharField(blank=True, default=None, max_length=200, verbose_name='Home Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='img_src',
            field=models.CharField(blank=True, default=None, max_length=200, verbose_name='Business Address'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='job_title',
            field=models.CharField(blank=True, default=None, max_length=20, verbose_name='Job Title'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=30, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='organization',
            field=models.CharField(blank=True, default=None, max_length=15, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone2',
            field=models.CharField(blank=True, default=None, max_length=20, verbose_name='Phone 2'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone3',
            field=models.CharField(blank=True, default=None, max_length=20, verbose_name='Phone 3'),
        ),
    ]
