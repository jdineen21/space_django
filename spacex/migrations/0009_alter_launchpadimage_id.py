# Generated by Django 3.2.3 on 2021-05-28 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacex', '0008_alter_launchpad_rockets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launchpadimage',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]