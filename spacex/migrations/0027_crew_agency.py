# Generated by Django 3.2.3 on 2021-05-30 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacex', '0026_launch_crew'),
    ]

    operations = [
        migrations.AddField(
            model_name='crew',
            name='agency',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
