# Generated by Django 3.2.3 on 2021-05-29 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacex', '0012_alter_core_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core',
            name='last_update',
            field=models.TextField(null=True),
        ),
    ]