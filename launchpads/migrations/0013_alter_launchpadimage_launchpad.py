# Generated by Django 3.2.3 on 2021-05-26 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('launchpads', '0012_launchpad_rockets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launchpadimage',
            name='launchpad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='launchpads.launchpad'),
        ),
    ]
