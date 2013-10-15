from django.template.response import TemplateResponse

from .models import Raffle


def home(request):
    raffles = Raffle.objects.exclude(n01__isnull=True)[:10]
    return TemplateResponse(request, 'megasena/home.html', {
        'raffles': raffles,
    })


def detail(request, number):
    last = Raffle.objects.exclude(n01__isnull=True).aggregate(Max('number'))['number__max']
    if int(number) <= last:
        infos = get_object_or_404(Raffle, number=number)
        return TemplateResponse(request, 'megasena/detail.html', {
            'infos': infos,
        })
    else:
        messages.add_message(request, messages.INFO, _('This concourse was not raffled yet'))
        return HttpResponseRedirect('/megasena')
