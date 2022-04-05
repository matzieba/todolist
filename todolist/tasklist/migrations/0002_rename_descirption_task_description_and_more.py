# Generated by Django 4.0.3 on 2022-04-05 08:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descirption',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='task',
            name='added_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
