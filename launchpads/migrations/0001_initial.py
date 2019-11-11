# Generated by Django 2.2.6 on 2019-11-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LaunchpadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.CharField(max_length=30)),
                ('image_location', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Launchpad Image',
                'verbose_name_plural': 'Launchpad Images',
            },
        ),
    ]
