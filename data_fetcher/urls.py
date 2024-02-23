from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('records', views.fetch_records, name='fetch_records'),
    path('countries',views.fetch_geoIds,name='fetch_geoIds'),
    path('countries_by_infectionrate', views.countries_by_infectionrate,name='countries_by_infectionrate'),
    path('total_stats_country',views.total_stats_country,name='total_stats_country'),
    path('countries_by_sum_cases', views.countries_by_sum_cases,name='countries_by_sum_cases'),
    path('countries_by_sum_deaths',views.countries_by_sum_deaths,name='countries_by_sum_deaths'),
    path('countries_by_cases_per_pop',views.countries_by_cases_per_pop,name='countries_by_cases_per_pop'),
    path('countries_by_deaths_per_pop',views.countries_by_deaths_per_pop,name='countries_by_deaths_per_pop'),
    path('countries_by_deathrate',views.countries_by_deathrate,name='countries_by_deathrate')
]
