from django import forms 
from .models import *

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'



class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'
