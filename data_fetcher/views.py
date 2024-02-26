from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import GeoDistribution, Records, Date
from django.db.models import Avg, Sum
from django.urls import reverse
from datetime import datetime
import django.core.serializers.json


# Create your views here.

def index(request):
    geo = get_list_or_404(GeoDistribution)
    dates = get_list_or_404(Date.objects.order_by('date_rep'))
    return render(request, 'data_fetcher/index.html',{'geo':geo , 'dates':dates})

def fetch_records(request):
    geo_ids = request.GET.getlist("country/territory[]")
    date_rep_min = request.GET["min_date_reps"]
    date_rep_max = request.GET["max_date_reps"]

    if("." in date_rep_min):
        date_rep_min_obj = datetime.strptime(date_rep_min,"%b. %d, %Y")
    else:
        date_rep_min_obj = datetime.strptime(date_rep_min,"%B %d, %Y")
    if("." in date_rep_max):
        date_rep_max_obj = datetime.strptime(date_rep_max,"%b. %d, %Y")
    else:
        date_rep_max_obj = datetime.strptime(date_rep_max,"%B %d, %Y")

    date_rep_min = date_rep_min_obj.strftime("%Y-%m-%d")
    date_rep_max = date_rep_max_obj.strftime("%Y-%m-%d")

    geo_names = []
    for geo_id in geo_ids:
        geo_name = GeoDistribution.objects.get(pk=geo_id).country_territory
        geo_names.append(geo_name);
    queries = [geo_names]

    for geo_id in geo_ids:
        query = list(Records.objects.filter(geo=geo_id) \
            .filter(date_rep__gte=date_rep_min) \
            .filter(date_rep__lte=date_rep_max) \
            .order_by("date_rep") \
            .values("date_rep","death_num","case_num","cum14d_infectionrate_100t") \
            .values_list())
        queries.append(query)

    for i in range(1,len(queries)):
        query = queries[i]
        for i in range(0,len(query)):
            ls = list(query[i])
            ls[0] = ls[0].strftime("%Y-%m-%d")
            ls = ls[0:1]+ls[2:]
            query[i] = ls
    return JsonResponse(queries,safe=False)


def countries_by_infectionrate(request):
    num_countries = int(request.GET["num_count"],10)
    date_rep_min = request.GET["min_date_reps"]
    date_rep_max = request.GET["max_date_reps"]
    continent = request.GET["continent"]
    order = request.GET["order"]

    if("." in date_rep_min):
        date_rep_min_obj = datetime.strptime(date_rep_min,"%b. %d, %Y")
    else:
        date_rep_min_obj = datetime.strptime(date_rep_min,"%B %d, %Y")
    if("." in date_rep_max):
        date_rep_max_obj = datetime.strptime(date_rep_max,"%b. %d, %Y")
    else:
        date_rep_max_obj = datetime.strptime(date_rep_max,"%B %d, %Y")

    date_rep_min = date_rep_min_obj.strftime("%Y-%m-%d")
    date_rep_max = date_rep_max_obj.strftime("%Y-%m-%d")

    if(continent != "None"):
        query = Records.objects.filter(date_rep__gte=date_rep_min).filter(date_rep__lte=date_rep_max) \
            .filter(geo_id__continent=continent).values('geo_id').annotate(avg_cum14d_infectionrate_100t=Avg('cum14d_infectionrate_100t'))
    else:
        query = Records.objects.filter(date_rep__gte=date_rep_min).filter(date_rep__lte=date_rep_max) \
            .values('geo_id').annotate(avg_cum14d_infectionrate_100t=Avg('cum14d_infectionrate_100t'))

    if(order=="desc"):
        query = query.order_by('-avg_cum14d_infectionrate_100t')
    else:
        query = query.order_by('avg_cum14d_infectionrate_100t')

    query = list(query)[:num_countries]
    query_list = []
    for dict in query:
        query_list.append([GeoDistribution.objects.get(pk=dict['geo_id']).country_territory,dict['avg_cum14d_infectionrate_100t']])

    return JsonResponse(query_list,safe=False)


def total_stats_country(request):
    geo_id = request.GET["country/territory"]
    query = Records.objects.filter(geo=geo_id).values('geo_id').annotate(sum_cases=Sum('case_num'), \
            sum_deaths=Sum('death_num'))
    geo = GeoDistribution.objects.get(pk=query[0]['geo_id'])
    sum_cases = query[0]['sum_cases']
    sum_deaths = query[0]['sum_deaths']
    query_list = [geo.country_territory, sum_cases,sum_deaths,sum_deaths/sum_cases,sum_cases/geo.pop2019*100,sum_deaths/geo.pop2019*100]
    return JsonResponse(query_list,safe=False)

def countries_by_sum_cases(request):

    num_countries = int(request.GET["num_count"],10)
    date_rep_min = request.GET["min_date_reps"]
    date_rep_max = request.GET["max_date_reps"]
    continent = request.GET["continent"]
    order = request.GET["order"]

    if("." in date_rep_min):
        date_rep_min_obj = datetime.strptime(date_rep_min,"%b. %d, %Y")
    else:
        date_rep_min_obj = datetime.strptime(date_rep_min,"%B %d, %Y")
    if("." in date_rep_max):
        date_rep_max_obj = datetime.strptime(date_rep_max,"%b. %d, %Y")
    else:
        date_rep_max_obj = datetime.strptime(date_rep_max,"%B %d, %Y")

    date_rep_min = date_rep_min_obj.strftime("%Y-%m-%d")
    date_rep_max = date_rep_max_obj.strftime("%Y-%m-%d")

    if(continent != "None"):
        query = Records.objects.filter(date_rep__gte=date_rep_min).filter(date_rep__lte=date_rep_max) \
        .filter(geo_id__continent=continent).values('geo_id').annotate(sum_cases=Sum('case_num'))
    else:
        query = Records.objects.filter(date_rep__gte=date_rep_min).filter(date_rep__lte=date_rep_max) \
        .values('geo_id').annotate(sum_cases=Sum('case_num'))

    if(order=="desc"):
        query = query.order_by('-sum_cases')
    else:
        query = query.order_by('sum_cases')

    query = list(query)[:num_countries]

    query_list = []
    for dict in query:
        query_list.append([GeoDistribution.objects.get(pk=dict['geo_id']).country_territory,dict['sum_cases']])

    return JsonResponse(query_list,safe=False)

def countries_by_sum_deaths(request):

    num_countries = int(request.GET["num_count"],10)
    date_rep_min = request.GET["min_date_reps"]
    date_rep_max = request.GET["max_date_reps"]
    continent = request.GET["continent"]
    order = request.GET["order"]

    if("." in date_rep_min):
        date_rep_min_obj = datetime.strptime(date_rep_min,"%b. %d, %Y")
    else:
        date_rep_min_obj = datetime.strptime(date_rep_min,"%B %d, %Y")
    if("." in date_rep_max):
        date_rep_max_obj = datetime.strptime(date_rep_max,"%b. %d, %Y")
    else:
        date_rep_max_obj = datetime.strptime(date_rep_max,"%B %d, %Y")

    date_rep_min = date_rep_min_obj.strftime("%Y-%m-%d")
    date_rep_max = date_rep_max_obj.strftime("%Y-%m-%d")

    if(continent != "None"):
        query = Records.objects.filter(date_rep__gte=date_rep_min).filter(date_rep__lte=date_rep_max) \
                .filter(geo_id__continent=continent).values('geo_id').annotate(sum_deaths=Sum('death_num'))
    else:
        query = Records.objects.filter(date_rep__gte=date_rep_min).filter(date_rep__lte=date_rep_max) \
                .values('geo_id').annotate(sum_deaths=Sum('death_num'))

    if(order=="desc"):
        query = query.order_by('-sum_deaths')
    else:
        query = query.order_by('sum_deaths')

    query = list(query)[:num_countries]

    query_list = []
    for dict in query:
        query_list.append([GeoDistribution.objects.get(pk=dict['geo_id']).country_territory,dict['sum_deaths']])
    return JsonResponse(query_list,safe=False)


def takeSecond(elem):
    return elem[1]

def countries_by_cases_per_pop(request):
    num_countries = int(request.GET["num_count"],10)
    date_rep_min = request.GET["min_date_reps"]
    date_rep_max = request.GET["max_date_reps"]
    continent = request.GET["continent"]
    order = request.GET["order"]

    if("." in date_rep_min):
        date_rep_min_obj = datetime.strptime(date_rep_min,"%b. %d, %Y")
    else:
        date_rep_min_obj = datetime.strptime(date_rep_min,"%B %d, %Y")
    if("." in date_rep_max):
        date_rep_max_obj = datetime.strptime(date_rep_max,"%b. %d, %Y")
    else:
        date_rep_max_obj = datetime.strptime(date_rep_max,"%B %d, %Y")

    date_rep_min = date_rep_min_obj.strftime("%Y-%m-%d")
    date_rep_max = date_rep_max_obj.strftime("%Y-%m-%d")

    if(continent!="None"):
        query = Records.objects.filter(date_rep__gte=date_rep_min).filter(date_rep__lte=date_rep_max) \
                .filter(geo_id__continent=continent).values('geo_id').annotate(sum_cases=Sum('case_num'))
    else:
        query = Records.objects.filter(date_rep__gte=date_rep_min).filter(date_rep__lte=date_rep_max) \
                .values('geo_id').annotate(sum_cases=Sum('case_num'))
    query = list(query)
    query_list = []
    for dict in query:
        geo = GeoDistribution.objects.get(pk=dict['geo_id'])
        query_list.append([geo.country_territory,dict['sum_cases']/geo.pop2019])
    if(order=='desc'):
        query_list.sort(reverse=True,key=takeSecond)
    else:
        query_list.sort(key=takeSecond)
    return JsonResponse(query_list[:num_countries],safe=False)

def countries_by_deaths_per_pop(request):
    num_countries = int(request.GET["num_count"],10)
    date_rep_min = request.GET["min_date_reps"]
    date_rep_max = request.GET["max_date_reps"]
    continent = request.GET["continent"]
    order = request.GET["order"]

    if("." in date_rep_min):
        date_rep_min_obj = datetime.strptime(date_rep_min,"%b. %d, %Y")
    else:
        date_rep_min_obj = datetime.strptime(date_rep_min,"%B %d, %Y")
    if("." in date_rep_max):
        date_rep_max_obj = datetime.strptime(date_rep_max,"%b. %d, %Y")
    else:
        date_rep_max_obj = datetime.strptime(date_rep_max,"%B %d, %Y")

    date_rep_min = date_rep_min_obj.strftime("%Y-%m-%d")
    date_rep_max = date_rep_max_obj.strftime("%Y-%m-%d")
    if(continent != "None"):
        query = Records.objects.filter(date_rep__gte=date_rep_min).filter(date_rep__lte=date_rep_max) \
            .filter(geo_id__continent=continent).values('geo_id').annotate(sum_deaths=Sum('death_num'))
    else:
        query = Records.objects.filter(date_rep__gte=date_rep_min).filter(date_rep__lte=date_rep_max) \
            .values('geo_id').annotate(sum_deaths=Sum('death_num'))
    query = list(query)
    query_list = []
    for dict in query:
        geo = GeoDistribution.objects.get(pk=dict['geo_id'])
        query_list.append([geo.country_territory,dict['sum_deaths']/geo.pop2019])
    if(order=="desc"):
        query_list.sort(reverse=True,key=takeSecond)
    else:
        query_list.sort(key=takeSecond)
    return JsonResponse(query_list[:num_countries],safe=False)

def countries_by_deathrate(request):
    num_countries = int(request.GET["num_count"],10)
    date_rep_min = request.GET["min_date_reps"]
    date_rep_max = request.GET["max_date_reps"]
    continent = request.GET["continent"]
    order = request.GET["order"]

    if("." in date_rep_min):
        date_rep_min_obj = datetime.strptime(date_rep_min,"%b. %d, %Y")
    else:
        date_rep_min_obj = datetime.strptime(date_rep_min,"%B %d, %Y")
    if("." in date_rep_max):
        date_rep_max_obj = datetime.strptime(date_rep_max,"%b. %d, %Y")
    else:
        date_rep_max_obj = datetime.strptime(date_rep_max,"%B %d, %Y")

    date_rep_min = date_rep_min_obj.strftime("%Y-%m-%d")
    date_rep_max = date_rep_max_obj.strftime("%Y-%m-%d")

    if(continent != "None"):
        query = Records.objects.filter(date_rep__gte=date_rep_min).filter(date_rep__lte=date_rep_max) \
                .filter(geo_id__continent=continent).values('geo_id').annotate(sum_cases=Sum('case_num'),sum_deaths=Sum('death_num'))
    else:
        query = Records.objects.filter(date_rep__gte=date_rep_min).filter(date_rep__lte=date_rep_max) \
                .values('geo_id').annotate(sum_cases=Sum('case_num'),sum_deaths=Sum('death_num'))

    query = list(query)
    query_list = []

    for dict in query:
        geo = GeoDistribution.objects.get(pk=dict['geo_id'])
        query_list.append([geo.country_territory,dict['sum_deaths']/dict['sum_cases']])
    if(order=="desc"):
        query_list.sort(reverse=True,key=takeSecond)
    else:
        query_list.sort(key=takeSecond)
    return JsonResponse(query_list[:num_countries],safe=False)

def fetch_geoIds(request):
    geo = get_list_or_404(GeoDistribution)
    return render(request, 'data_fetcher/geo_ids.html', {'geo': geo})
