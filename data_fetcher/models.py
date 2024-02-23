from django.db import models


class Date(models.Model):
    date_rep = models.DateField(primary_key=True)
    day = models.BigIntegerField(blank=True, null=True)
    month = models.BigIntegerField(blank=True, null=True)
    year = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'date'


class GeoDistribution(models.Model):
    geo_id = models.TextField(primary_key=True)
    country_territory = models.TextField(db_column='country/territory', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    country_territory_code = models.TextField(db_column='country/territory_code', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    pop2019 = models.FloatField(blank=True, null=True)
    continent = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'geo_distribution'


class Records(models.Model):
    date_rep = models.OneToOneField(Date, models.DO_NOTHING, db_column='date_rep', primary_key=True)
    geo = models.ForeignKey(GeoDistribution, models.DO_NOTHING)
    case_num = models.BigIntegerField(blank=True, null=True)
    death_num = models.BigIntegerField(blank=True, null=True)
    cum14d_infectionrate_100t = models.FloatField(db_column='cum14D_infectionrate/100T', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'records'
        unique_together = (('date_rep', 'geo'),)
