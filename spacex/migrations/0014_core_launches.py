# Generated by Django 3.2.3 on 2021-05-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacex', '0013_alter_core_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='core',
            name='launches',
            field=models.ManyToManyField(to='spacex.Launch'),
        ),
    ]
