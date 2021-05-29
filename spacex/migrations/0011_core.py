# Generated by Django 3.2.3 on 2021-05-29 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spacex', '0010_alter_launchpadimage_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Core',
            fields=[
                ('block', models.IntegerField()),
                ('reuse_count', models.IntegerField(null=True)),
                ('rtls_attempts', models.IntegerField(null=True)),
                ('rtls_landings', models.IntegerField(null=True)),
                ('asds_attempts', models.IntegerField(null=True)),
                ('asds_landings', models.IntegerField(null=True)),
                ('last_update', models.TextField()),
                ('serial', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Core',
                'verbose_name_plural': 'Cores',
            },
        ),
    ]