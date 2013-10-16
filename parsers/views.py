from django.contrib import messages
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _

from megasena.models import Files

from .forms import UploadFileForm
from .parser import open_local_file


def parse_megasena(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = Files(file=request.FILES['file'])
            file.save()
            return HttpResponseRedirect('/parse/parse_file/')

    args = {}
    args.update(csrf(request))
    args['form'] = UploadFileForm()
    args['title'] = _("Upload zip file")
    args['class'] = 'files'
    args['extra'] = 'multipart/form-data'
    args['operation'] = _("Update Games")

    return TemplateResponse(request, 'megasena/form.html', args)


def parse_file(request):
    created = open_local_file()
    message = ''
    if created:
        message = _('New games were added')
    else:
        message = _('The games are up to date')
    messages.add_message(request, messages.INFO, message)
    return HttpResponseRedirect('/megasena/')
