# Generated by Django 3.2.3 on 2021-05-27 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacex', '0006_auto_20210527_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='launch',
            name='sanitized_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
