# Generated by Django 4.0.3 on 2022-04-06 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0007_alter_task_added_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='prio',
            field=models.CharField(choices=[('low', 'delete?'), ('regular', 'needs to be done'), ('high', 'are you?')], default='low', max_length=20),
        ),
    ]
