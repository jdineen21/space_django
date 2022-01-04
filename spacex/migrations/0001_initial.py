# Generated by Django 4.0 on 2022-01-04 23:31

from django.db import migrations, models
import django.db.models.deletion
import spacex.models.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('sanitized_name', models.CharField(max_length=100)),
                ('agency', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('wikipedia', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Crew',
                'verbose_name_plural': 'Crew',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('source', models.URLField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('patch', 'Patch'), ('image', 'Image'), ('portrait', 'Portrait')], max_length=10)),
                ('etag', models.CharField(max_length=100)),
                ('image', models.ImageField(height_field='height', upload_to=spacex.models.image.image_directory_path, width_field='width')),
                ('height', models.IntegerField(null=True)),
                ('width', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Launch',
            fields=[
                ('significant', models.BooleanField(default=False)),
                ('fairings', models.JSONField(blank=True, null=True)),
                ('links', models.JSONField()),
                ('static_fire_date_utc', models.DateTimeField(blank=True, null=True)),
                ('static_fire_date_unix', models.IntegerField(blank=True, null=True)),
                ('tbd', models.BooleanField()),
                ('net', models.BooleanField()),
                ('window', models.IntegerField(blank=True, null=True)),
                ('success', models.BooleanField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('auto_update', models.BooleanField()),
                ('launch_library_id', models.CharField(blank=True, max_length=100, null=True)),
                ('flight_number', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('sanitized_name', models.CharField(max_length=100)),
                ('date_utc', models.DateTimeField(blank=True, null=True)),
                ('date_unix', models.IntegerField(blank=True, null=True)),
                ('date_local', models.DateTimeField(blank=True, null=True)),
                ('date_precision', models.CharField(blank=True, max_length=100, null=True)),
                ('upcoming', models.BooleanField()),
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('crew', models.ManyToManyField(to='spacex.Crew')),
                ('images', models.ManyToManyField(to='spacex.Image')),
            ],
            options={
                'verbose_name': 'launch',
                'verbose_name_plural': 'launches',
                'ordering': ['flight_number'],
            },
        ),
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
                ('images', models.ManyToManyField(to='spacex.Image')),
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
                ('sanitized_name', models.CharField(max_length=100)),
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
                ('images', models.ManyToManyField(to='spacex.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Payload',
            fields=[
                ('dragon', models.JSONField()),
                ('name', models.CharField(max_length=100)),
                ('sanitized_name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('reused', models.BooleanField()),
                ('customers', models.JSONField()),
                ('norad_ids', models.JSONField(blank=True, null=True)),
                ('nationalities', models.JSONField()),
                ('manufacturers', models.JSONField()),
                ('mass_kg', models.FloatField(blank=True, null=True)),
                ('mass_lbs', models.FloatField(blank=True, null=True)),
                ('orbit', models.CharField(blank=True, max_length=100, null=True)),
                ('reference_system', models.CharField(blank=True, max_length=100, null=True)),
                ('regime', models.CharField(blank=True, max_length=100, null=True)),
                ('lifespan_years', models.IntegerField(blank=True, null=True)),
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('launch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spacex.launch')),
            ],
            options={
                'verbose_name': 'Payload',
                'verbose_name_plural': 'Payloads',
            },
        ),
        migrations.CreateModel(
            name='LaunchpadImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
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
        migrations.AddField(
            model_name='launch',
            name='launchpad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spacex.launchpad'),
        ),
        migrations.AddField(
            model_name='launch',
            name='rocket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='spacex.rocket'),
        ),
        migrations.CreateModel(
            name='Landpad',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('sanitized_name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('locality', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('landing_attempts', models.IntegerField()),
                ('landing_successes', models.IntegerField()),
                ('wikipedia', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('images', models.ManyToManyField(to='spacex.Image')),
            ],
            options={
                'verbose_name': 'Landpad',
                'verbose_name_plural': 'Landpads',
            },
        ),
        migrations.CreateModel(
            name='Dragon',
            fields=[
                ('heat_shield', models.JSONField()),
                ('launch_payload_mass', models.JSONField()),
                ('launch_payload_vol', models.JSONField()),
                ('return_payload_mass', models.JSONField()),
                ('return_payload_vol', models.JSONField()),
                ('pressurized_capsule', models.JSONField()),
                ('trunk', models.JSONField()),
                ('height_w_trunk', models.JSONField()),
                ('diameter', models.JSONField()),
                ('first_flight', models.DateField()),
                ('flickr_images', models.JSONField()),
                ('name', models.CharField(max_length=100)),
                ('sanitized_name', models.CharField(max_length=100)),
                ('active', models.BooleanField()),
                ('crew_capacity', models.IntegerField()),
                ('sidewall_angle_deg', models.IntegerField()),
                ('orbit_duration_yr', models.IntegerField()),
                ('dry_mass_kg', models.IntegerField()),
                ('dry_mass_lb', models.IntegerField()),
                ('thrusters', models.JSONField()),
                ('wikipedia', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('images', models.ManyToManyField(to='spacex.Image')),
            ],
            options={
                'verbose_name': 'Dragon',
                'verbose_name_plural': 'Dragons',
            },
        ),
        migrations.AddField(
            model_name='crew',
            name='images',
            field=models.ManyToManyField(to='spacex.Image'),
        ),
        migrations.CreateModel(
            name='Core',
            fields=[
                ('block', models.IntegerField(blank=True, null=True)),
                ('reuse_count', models.IntegerField(blank=True, null=True)),
                ('rtls_attempts', models.IntegerField(blank=True, null=True)),
                ('rtls_landings', models.IntegerField(blank=True, null=True)),
                ('asds_attempts', models.IntegerField(blank=True, null=True)),
                ('asds_landings', models.IntegerField(blank=True, null=True)),
                ('last_update', models.TextField(blank=True, null=True)),
                ('serial', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=100)),
                ('id', models.CharField(max_length=24, primary_key=True, serialize=False)),
                ('launches', models.ManyToManyField(to='spacex.Launch')),
            ],
            options={
                'verbose_name': 'Core',
                'verbose_name_plural': 'Cores',
            },
        ),
    ]
