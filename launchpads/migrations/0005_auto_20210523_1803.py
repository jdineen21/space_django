# Generated by Django 3.2.3 on 2021-05-23 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchpads', '0004_rename_logitude_launchpad_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launchpad',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='launchpad',
            name='longitude',
            field=models.FloatField(),
        ),
    ]
