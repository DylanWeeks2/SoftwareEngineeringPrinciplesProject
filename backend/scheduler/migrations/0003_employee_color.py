# Generated by Django 2.2.6 on 2019-10-22 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_remove_location_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='color',
            field=models.CharField(default='#000000', max_length=7),
            preserve_default=False,
        ),
    ]