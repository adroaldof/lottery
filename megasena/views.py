from django.contrib import messages
from django.core.context_processors import csrf
from django.db.models import Max
from django.forms.formsets import formset_factory, BaseFormSet
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _


from .forms import ConcourseForm, BetForm, BetFormset
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
        messages.add_message(
            request, messages.INFO, _('This concourse was not raffled yet')
        )
        return HttpResponseRedirect('/megasena')


def bets(request):
    infos = Bet.objects.all()
    return TemplateResponse(request, 'megasena/bets.html', {
        'infos': infos,
    })


def create(request):
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
            concourse, s = Concourse.objects.get_or_create(**form.cleaned_data)
            for form in formset.forms:
                form = form.save(commit=False)
                form.number = concourse
                form.save()
            messages.add_message(
                request, messages.INFO, _('Bet was successfully added')
            )
            return HttpResponseRedirect('/megasena/bets')

    args = {}
    args.update(csrf(request))
    args['form'] = ConcourseForm()
    args['formset'] = Formset()
    args['title'] = _("Add Your Bet")
    args['class'] = 'add'
    args['operation'] = _("Add Game")

    return TemplateResponse(request, 'megasena/form.html', args)


def update(request, number):
    concourse = get_object_or_404(Concourse, number=number)

    if request.method == 'POST':
        formset = BetFormset(request.POST, request.FILES, instance=concourse)
        if formset.is_valid():
            formset.save()
            messages.add_message(
                request, messages.INFO, _('Bet was successfully updated')
            )
            return HttpResponseRedirect('/megasena/bets')

    args = {}
    args.update(csrf(request))
    args['formset'] = BetFormset(instance=concourse)
    args['title'] = _("Update Your Bet")
    args['class'] = 'update'
    args['operation'] = _("Update Game")

    return TemplateResponse(request, 'megasena/form.html', args)


def delete(request, pk):
    bet = get_object_or_404(Bet, id=pk)

    if bet:
        bet.delete()
        messages.add_message(
            request, messages.INFO, _('Bet was sucessfully deleted')
        )
        return HttpResponseRedirect('/megasena/bets')


def check(request, number):
    last = Raffle.objects.exclude(n01__isnull=True).aggregate(Max('number'))
    if last['number__max'] is None or last['number__max'] < int(number):
        print '\nIs not none'
        messages.add_message(
            request, messages.INFO, _('This concourse was not raffled yet')
        )
        return HttpResponseRedirect('/megasena/bets')
    else:
        if last['number__max'] >= int(number):
            concourse = get_object_or_404(Concourse, number=number)
            raffled = concourse.raffle_set.all()
            bets = concourse.bet_set.all()
            return TemplateResponse(request, 'megasena/check.html', {
                'raffled': raffled,
                'bets': bets
            })
