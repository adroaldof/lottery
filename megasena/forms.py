from django import forms
from django.forms.models import inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from .models import Concourse, Bet


class ConcourseForm(forms.Form):
    STUBBORNS = (
        ('0', '-----'),
        ('2', 'Two'),
        ('4', 'Four'),
        ('8', 'Eight'),
    )
    concourse = forms.CharField(max_length=4, label=_('Concourse'))
    stubborns = forms.ChoiceField(choices=STUBBORNS)

    class Meta:
        model = Concourse
        fields = ('concourse',)


class BetForm(forms.ModelForm):
    n01 = forms.CharField(max_length=2, label='')
    n02 = forms.CharField(max_length=2, label='')
    n03 = forms.CharField(max_length=2, label='')
    n04 = forms.CharField(max_length=2, label='')
    n05 = forms.CharField(max_length=2, label='')
    n06 = forms.CharField(max_length=2, label='')

    class Meta:
        model = Bet
        exclude = ('concourse', 'stubborns', 'hits',)


BetFormset = inlineformset_factory(
    Concourse, Bet, form=BetForm, can_delete=True, extra=0
)


class UploadFileForm(forms.Form):
    file = forms.FileField(label=_("Select a file"))
