# Generated by Django 3.0.8 on 2020-07-19 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_auto_20200720_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='uuid',
        ),
    ]
