# Generated by Django 4.0.3 on 2022-04-08 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainprojects', '0002_mainproject_delete_task'),
        ('tasklist', '0010_task_main_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='main_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainprojects.mainproject'),
        ),
    ]
