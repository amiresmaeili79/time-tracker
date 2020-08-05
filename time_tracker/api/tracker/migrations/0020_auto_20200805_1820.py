# Generated by Django 3.0.8 on 2020-08-05 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0019_auto_20200805_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project_id',
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.Project'),
        ),
    ]