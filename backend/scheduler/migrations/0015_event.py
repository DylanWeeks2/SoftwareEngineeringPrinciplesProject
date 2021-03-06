# Generated by Django 2.2.6 on 2019-11-21 08:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0014_employeeassignment_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('event_start', models.DateTimeField(default=django.utils.timezone.now)),
                ('event_end', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
