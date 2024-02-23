# Generated by Django 5.0.2 on 2024-02-20 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('date_rep', models.DateField(primary_key=True, serialize=False)),
                ('day', models.BigIntegerField(blank=True, null=True)),
                ('month', models.BigIntegerField(blank=True, null=True)),
                ('year', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'date',
            },
        ),
        migrations.CreateModel(
            name='GeoDistribution',
            fields=[
                ('geo_id', models.TextField(primary_key=True, serialize=False)),
                ('country_territory', models.TextField(blank=True, db_column='country/territory', null=True)),
                ('country_territory_code', models.TextField(blank=True, db_column='country/territory_code', null=True)),
                ('pop2019', models.FloatField(blank=True, null=True)),
                ('continent', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'geo_distribution',
            },
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('date_rep', models.OneToOneField(db_column='date_rep', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='data_fetcher.date')),
                ('case_num', models.BigIntegerField(blank=True, null=True)),
                ('death_num', models.BigIntegerField(blank=True, null=True)),
                ('cum14d_infectionrate_100t', models.FloatField(blank=True, db_column='cum14D_infectionrate/100T', null=True)),
                ('geo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='data_fetcher.geodistribution')),
            ],
            options={
                'db_table': 'records',
                'unique_together': {('date_rep', 'geo')},
            },
        ),
    ]
