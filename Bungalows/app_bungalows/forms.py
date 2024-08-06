from django import forms
from django.forms import widgets, ModelForm
from django.forms.utils import ErrorList
from app_bungalows.models import Bungalow
from django.db import transaction

class BungalowCopyForm(forms.Form):
    name = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")

        super(BungalowCopyForm, self).__init__(*args, **kwargs)
        active_b_id = self.request.session['bungalow_active']
        self.fields['name'].queryset = Bungalow.objects.exclude(id=active_b_id)