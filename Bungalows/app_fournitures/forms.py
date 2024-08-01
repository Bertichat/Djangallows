from django import forms
from django.forms import widgets, ModelForm
from .models import *
from django.db import transaction


class createFournitureForm(ModelForm):
    class Meta:
        model = Fourniture
        fields = ("name", "compte_base")
        labels = {"name":'Nom', "compte_base":"total actuel"}

class updateFournitureForm(ModelForm):
    class Meta:
        model = Fourniture
        fields = ("compte_base",)
        labels = {"compte_base":""}
