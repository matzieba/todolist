# Generated by Django 4.0.3 on 2022-04-08 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainprojects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('added_date', models.DateField(default=datetime.date.today)),
                ('description', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('in pipeline', 'in pipeline'), ('done', 'done')], default='in pipeline', max_length=20)),
                ('added_by', models.CharField(max_length=100)),
                ('prio', models.CharField(choices=[('low', 'low'), ('regular', 'regular'), ('high', 'high')], default='low', max_length=20)),
                ('proceed_till', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]