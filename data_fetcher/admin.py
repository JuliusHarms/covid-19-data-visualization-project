from django.contrib import admin
from .models import Date,GeoDistribution,Records
# Register your models here.
admin.site.register(Date)
admin.site.register(GeoDistribution)
admin.site.register(Records)
