from django.contrib import messages
from django.core.context_processors import csrf
from django.db.models import Max
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _


from .forms import ConcourseForm, BetForm
from .models import Concourse, Raffle, Bet


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


def list(request):
    infos = Bet.objects.all()
    return TemplateResponse(request, 'megasena/list.html', {
        'infos': infos,
    })


def add(request):
    class RequiredFormSet(BaseFormSet):
        def __init__(self, *args, **kwargs):
            super(RequiredFormSet, self).__init__(*args, **kwargs)
            for form in self.forms:
                form.empty_permitted = False

    Formset = formset_factory(
        BetForm, max_num=10, formset=RequiredFormSet
    )

    if request.method == 'POST':
        form = ConcourseForm(request.POST)
        formset = Formset(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            concourse, success = Concourse.objects.get_or_create(**form.cleaned_data)
            for form in formset.forms:
                form = form.save(commit=False)
                form.number = concourse
                form.save()
            messages.add_message(
                request, messages.INFO, _('Game was added successfully.')
            )
            return HttpResponseRedirect('/megasena/list')

    args = {}
    args.update(csrf(request))
    args['form'] = ConcourseForm()
    args['formset'] = Formset()
    args['title'] = _("Add Your Bet")
    args['class'] = 'add'
    args['operation'] = _("Add Game")

    return TemplateResponse(request, 'megasena/form.html', args)

