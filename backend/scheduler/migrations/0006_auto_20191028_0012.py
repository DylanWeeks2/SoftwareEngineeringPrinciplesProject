# Generated by Django 2.2.6 on 2019-10-28 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_auto_20191027_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='fri_end',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='fri_start',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='monday_end',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='monday_start',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sat_end',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sat_start',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sun_end',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sun_start',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='thu_end',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='thu_start',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='tue_end',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='tue_start',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='wed_end',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='wed_start',
            field=models.TimeField(default='00:00:00'),
        ),
    ]
