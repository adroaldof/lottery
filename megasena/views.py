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
    conc = get_object_or_404(Concourse, concourse=concourse)
    bets = Bet.objects.filter(concourse=conc)
    concourses = [int(concourse)]

    for bet in bets:
        for stubborn in range(int(concourse), int(concourse) + bet.stubborns):
            if stubborn not in concourses:
                concourses.append(stubborn)

    raffles = Raffle.objects.filter(concourse__in=concourses)
    return TemplateResponse(request, 'megasena/check.html', {
        'bets': bets,
        'raffles': raffles,
    })


def check_all(request):
    message = _("No luck this time, may be next concourse")
    hits = 0
    bet_objects = Bet.objects.all()
    raffle_objects = Raffle.objects.all()
    last = raffle_objects.aggregate(Max('concourse'))['concourse__max']

    for bet_object in bet_objects:
        bet_object.hits = 0
        bet_object.save()
        concourse = bet_object.concourse.concourse
        for current_bet in range(concourse, concourse+bet_object.stubborns):
            if current_bet <= last:
                raffled = raffle_objects.get(concourse=current_bet)
                raffles = [
                    raffled.n01, raffled.n02, raffled.n03,
                    raffled.n04, raffled.n05, raffled.n06
                ]
                bets = [
                    bet_object.n01, bet_object.n02, bet_object.n03,
                    bet_object.n04, bet_object.n05, bet_object.n06
                ]

                for raffled_number in raffles:
                    for bet_number in bets:
                        if raffled_number == bet_number:
                            hits += 1

                if hits > bet_object.hits:
                    bet_object.hits = hits
                    bet_object.save()

                if (hits > 3):
                    message = _("Awesome! You are the locky one. Congrats!")
                hits = 0

    messages.add_message(request, messages.INFO, message)
    return HttpResponseRedirect('/megasena/bets')
