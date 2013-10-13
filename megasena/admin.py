from django.contrib import admin

from .models import Concourse, Raffle, Bet


admin.site.register(Concourse)
admin.site.register(Raffle)
admin.site.register(Bet)
