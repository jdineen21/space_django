# Generated by Django 3.2.3 on 2021-06-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacex', '0003_auto_20210619_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='launch',
            name='images',
            field=models.ManyToManyField(to='spacex.Image'),
        ),
    ]
