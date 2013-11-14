from django.contrib import admin

from .models import Concourse, Raffle, Bet


class ConcourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Concourse Information', {'fields': ['concourse']}),
    ]


class RaffleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Concourse Informatioin', {'fields': ['concourse', 'raffle_date',]}),
        ('Raffled Numbers', {
            'fields': ['n01', 'n02', 'n03', 'n04', 'n05', 'n06',]
        }),
        ('Money Amount', {'fields': ['collected_amount',]}),
        ('Sena', {'fields': ['sena_winners', 'sena_share',]}),
        ('Quina', {'fields': ['quina_winners', 'quina_share',]}),
        ('Quadra', {'fields': ['quadra_winners', 'quadra_share',]}),
        ('Accumulated', {
            'fields': ['accumulated_status', 'accumulated_value', 'prize_next']
        }),
        ('Turnaround Prize', {'fields': ['prize_turnaround',]}),
    ]
    list_display = (
        'concourse', 'raffle_date', 'n01', 'n02', 'n03', 'n04', 'n05', 'n06',
        'sena_winners', 'sena_share', 'accumulated_value', 'prize_next',
        'prize_turnaround',
    )
    list_filter = ['raffle_date', 'accumulated_status',]
    search_fields = ['concourse',]
    date_hierarchy = 'raffle_date'


class BetAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Concourse Informatioin', {'fields': ['concourse',]}),
        ('Raffled Numbers', {
            'fields': ['n01', 'n02', 'n03', 'n04', 'n05', 'n06',]
        }),
        ('Bet Informaion', {'fields': {'hits', 'stubborns'}})
    ]
    list_display = (
        'concourse', 'n01', 'n02', 'n03', 'n04', 'n05', 'n06', 'hits', 'stubborns'
    )
    search_fields = ['concourse',]


admin.site.register(Concourse, ConcourseAdmin)
admin.site.register(Raffle, RaffleAdmin)
admin.site.register(Bet, BetAdmin)
