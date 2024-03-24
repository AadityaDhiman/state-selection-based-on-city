from django.urls import path
from.views import *

urlpatterns = [
    path('create-state',create_state, name="create-state"),
    path('create-city',create_city, name="create-state"),
    path('create-area',create_area, name="create-state"),
    path('get-cities/',get_cities,name='get-cities'),
    path('get-area/',get_area,name='get-area'),
    path('get-state/',get_state,name='get-state')

]
