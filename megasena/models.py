from django.db import models


class Files(models.Model):
    file = models.FileField(upload_to='megasena/')


class Concourse(models.Model):
    number = models.IntegerField(max_length=4, unique=True)

    class Meta:
        ordering = ['-number']

    def __unicode__(self):
        return u"%s" % self.number


class Raffle(models.Model):
    number = models.ForeignKey(Concourse)
    raffle_date = models.DateField(null=True, blank=True)
    n01 = models.IntegerField(max_length=2, null=True, blank=True)
    n02 = models.IntegerField(max_length=2, null=True, blank=True)
    n03 = models.IntegerField(max_length=2, null=True, blank=True)
    n04 = models.IntegerField(max_length=2, null=True, blank=True)
    n05 = models.IntegerField(max_length=2, null=True, blank=True)
    n06 = models.IntegerField(max_length=2, null=True, blank=True)
    collected_amount = models.FloatField(null=True, blank=True)
    sena_winners = models.IntegerField(max_length=5, null=True, blank=True)
    sena_share = models.FloatField(null=True, blank=True)
    quina_winners = models.IntegerField(max_length=5, null=True, blank=True)
    quina_share = models.FloatField(null=True, blank=True)
    quadra_winners = models.IntegerField(max_length=5, null=True, blank=True)
    quadra_share = models.FloatField(null=True, blank=True)
    accumulated_status = models.BooleanField(blank=True)
    accumulated_value = models.FloatField(null=True, blank=True)
    prize_next = models.FloatField(null=True, blank=True)
    prize_turnaround = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['-raffle_date']

    def __unicode__(self):
        return u"%s %s" % (self.number, self.raffle_date)


class Bet(models.Model):
    number = models.ForeignKey(Concourse)
    n01 = models.IntegerField(max_length=2)
    n02 = models.IntegerField(max_length=2)
    n03 = models.IntegerField(max_length=2)
    n04 = models.IntegerField(max_length=2)
    n05 = models.IntegerField(max_length=2)
    n06 = models.IntegerField(max_length=2)
    hits = models.IntegerField(max_length=1, blank=True, null=True)

    class Meta:
        ordering = ['-hits', 'number']

    def __unicode__(self):
        return u"%s" % self.number
