from django.shortcuts import render, HttpResponse
from .forms import *
from django.http import JsonResponse
# Create your views here.

# here will be state insert code
def create_state(request):
    context = {}
    if request.method == 'GET':
        form = StateForm()
        context['form'] = form
        return render(request, 'index.html',context)
    
    if request.method == 'POST':
        form = StateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("create Success")

# here will be city insert code
def create_city(request):
    context = {}
    if request.method == 'GET':
        form = CityForm()
        context['form'] = form
        return render(request, 'index.html',context)
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("create Success")

# here will be area insert code
def create_area(request):
    context = {}
    if request.method == 'GET':
        form = AreaForm()
        context['form'] = form
        return render(request, 'index.html',context)
    if request.method == 'POST':
            form = AreaForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse("create Success")


def get_state(request):
    context = {}
    if request.method == 'GET':
        items  = State.objects.all() 
        context['items'] = items
        return render(request, 'index.html', context)

# get cities will be on dependent in the state
def get_cities(request):
    country_id = request.GET.get('state_id')
    items = City.objects.filter(country_name_id=country_id).values('id','name')
    return JsonResponse(list(items),safe=False)

# get area will be on dependent in the cities
def get_area(request):
    city_id = request.GET.get('city_id')
    items = Area.objects.filter(city_name_id=city_id).values('id','name')
    return JsonResponse(list(items),safe=False)    