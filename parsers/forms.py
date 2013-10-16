from django import forms
from django.utils.translation import ugettext_lazy as _


class UploadFileForm(forms.Form):
    file = forms.FileField(label=_("Select a file"))
