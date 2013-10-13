from django.db import models
from django.utils.translation import ugettext_lazy as _


class Concourse(models.Model):
    number = models.IntegerField()


class Raffle(models.Model):
    number = models.ForeignKey(Concourse)
    raffle_date = models.DateField()
    n01 = models.IntegerField()
    n02 = models.IntegerField()
    n03 = models.IntegerField()
    n04 = models.IntegerField()
    n05 = models.IntegerField()
    n06 = models.IntegerField()
    collected_amount = models.FloatField()
    sena_winners = models.IntegerField()
    sena_share = models.FloatField()
    quina_winners = models.IntegerField()
    quina_share = models.FloatField()
    quadra_winners = models.IntegerField()
    quadra_share = models.FloatField()
    accumulated_status = models.BooleanField()
    accumulated_value = models.FloatField()
    prize_next = models.FloatField()
    prize_turnaround = models.FloatField()


class Bet(models.Model):
    number = models.ForeignKey(Concourse)
    n01 = models.IntegerField()
    n02 = models.IntegerField()
    n03 = models.IntegerField()
    n04 = models.IntegerField()
    n05 = models.IntegerField()
    n06 = models.IntegerField()
    hits = models.IntegerField()
