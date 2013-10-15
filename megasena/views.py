from django.template.response import TemplateResponse

from .models import Raffle


def home(request):
    raffles = Raffle.objects.exclude(n01__isnull=True)[:10]
    return TemplateResponse(request, 'megasena/home.html', {
        'raffles': raffles,
    })
