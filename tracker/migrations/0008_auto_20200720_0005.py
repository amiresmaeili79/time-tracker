# Generated by Django 3.0.8 on 2020-07-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20200720_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]