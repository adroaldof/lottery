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


def detail(request, concourse):
    last = Raffle.objects.all().aggregate(Max('concourse'))['concourse__max']
    if int(concourse) <= last:
        infos = get_object_or_404(Raffle, concourse=concourse)
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
        main_form = ConcourseForm(request.POST)
        formset = Formset(request.POST, request.FILES)
        if main_form.is_valid() and formset.is_valid():
            concourse, s = Concourse.objects.get_or_create(
                concourse=main_form.cleaned_data.get('concourse')
            )
            for form in formset.forms:
                form = form.save(commit=False)
                form.concourse = concourse
                form.stubborns = main_form.cleaned_data.get('stubborns')
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


def update(request, concourse):
    concourse = get_object_or_404(Concourse, concourse=concourse)

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


def change_stubborns(request, pk, value):
    bet = get_object_or_404(Bet, id=pk)

    bet.stubborns = value
    bet.save()

    return HttpResponseRedirect('/megasena/bets')


def check(request, concourse):
    last = Raffle.objects.exclude(n01__isnull=True).aggregate(Max('concourse'))
    if last['concourse__max'] is None or last['concourse__max'] < int(concourse):
        messages.add_message(
            request, messages.INFO, _('This concourse was not raffled yet')
        )
        return HttpResponseRedirect('/megasena/bets')
    else:
        if last['concourse__max'] >= int(concourse):
            concourse = get_object_or_404(Concourse, concourse=concourse)
            raffled = concourse.raffle_set.all()
            bets = concourse.bet_set.all()
            return TemplateResponse(request, 'megasena/check.html', {
                'raffled': raffled,
                'bets': bets
            })


def check_all(request):
    message = _("No luck this time, may be next concourse")
    hits = 0
    bets = Bet.objects.all()

    for bet in bets:
        raffled = Raffle.objects.all()
        last = raffled.aggregate(Max('concourse'))['concourse__max']
        if bet.hits is None and bet.concourse.concourse <= last:
            curr = raffled.get(concourse=bet.concourse)
            concourses = [
                curr.n01, curr.n02, curr.n03, curr.n04, curr.n05, curr.n06
            ]
            bets = [bet.n01, bet.n02, bet.n03, bet.n04, bet.n05, bet.n06]

            for s in concourses:
                for b in bets:
                    if s == b:
                        hits += 1

            bet.hits = hits
            bet.save()

            if (hits > 3):
                message = _("Awesome! You are a lucky person, you won a prize")
            hits = 0

    messages.add_message(request, messages.INFO, message)
    return HttpResponseRedirect('/megasena/bets')
