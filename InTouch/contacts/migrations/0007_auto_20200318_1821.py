# Generated by Django 3.0.4 on 2020-03-18 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20200318_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='img_src',
            field=models.CharField(blank=True, default='https://imgur.com/a/WbbsBB6', max_length=200, null=True, verbose_name='Business Address'),
        ),
    ]
