# Generated by Django 4.0.3 on 2022-04-05 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0006_alter_task_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='added_by',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]