from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Concourse, Bet


class ConcourseForm(forms.ModelForm):
    number = forms.CharField(max_length=4, label=_('Concourse'))

    class Meta:
        model = Concourse
        fields = ('number',)


class BetForm(forms.ModelForm):
    n01 = forms.CharField(max_length=2, label='')
    n02 = forms.CharField(max_length=2, label='')
    n03 = forms.CharField(max_length=2, label='')
    n04 = forms.CharField(max_length=2, label='')
    n05 = forms.CharField(max_length=2, label='')
    n06 = forms.CharField(max_length=2, label='')

    class Meta:
        model = Bet
        exclude = ('number', 'stubborn', 'hits',)
