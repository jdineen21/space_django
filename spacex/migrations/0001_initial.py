# Generated by Django 3.2.3 on 2021-05-26 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Launchpad',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('sanitized_name', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('timezone', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('launch_attempts', models.IntegerField()),
                ('launch_successes', models.IntegerField()),
                ('details', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Launchpad',
                'verbose_name_plural': 'Launchpads',
            },
        ),
        migrations.CreateModel(
            name='Rocket',
            fields=[
                ('height', models.JSONField()),
                ('diameter', models.JSONField()),
                ('mass', models.JSONField()),
                ('first_stage', models.JSONField()),
                ('second_stage', models.JSONField()),
                ('engines', models.JSONField()),
                ('landing_legs', models.JSONField()),
                ('payload_weights', models.JSONField()),
                ('flickr_images', models.JSONField()),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('active', models.BooleanField()),
                ('stages', models.IntegerField()),
                ('boosters', models.IntegerField()),
                ('cost_per_launch', models.IntegerField()),
                ('success_rate_pct', models.IntegerField()),
                ('first_flight', models.DateField()),
                ('country', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('wikipedia', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='LaunchpadImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_location', models.CharField(max_length=200)),
                ('launchpad', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='spacex.launchpad')),
            ],
            options={
                'verbose_name': 'Launchpad Image',
                'verbose_name_plural': 'Launchpad Images',
            },
        ),
        migrations.AddField(
            model_name='launchpad',
            name='rockets',
            field=models.ManyToManyField(to='spacex.Rocket'),
        ),
        migrations.CreateModel(
            name='Launch',
            fields=[
                ('fairings', models.JSONField(null=True)),
                ('links', models.JSONField()),
                ('static_fire_date_utc', models.DateTimeField(null=True)),
                ('static_fire_date_unix', models.IntegerField(null=True)),
                ('tbd', models.BooleanField()),
                ('net', models.BooleanField()),
                ('window', models.IntegerField(null=True)),
                ('success', models.BooleanField(null=True)),
                ('details', models.TextField(null=True)),
                ('auto_update', models.BooleanField()),
                ('launch_library_id', models.CharField(max_length=100, null=True)),
                ('flight_number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('date_utc', models.DateTimeField(null=True)),
                ('date_unix', models.IntegerField(null=True)),
                ('date_local', models.DateTimeField(null=True)),
                ('date_precision', models.CharField(max_length=100, null=True)),
                ('upcoming', models.BooleanField()),
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('launchpad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spacex.launchpad')),
                ('rocket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spacex.rocket')),
            ],
        ),
    ]
