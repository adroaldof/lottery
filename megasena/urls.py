from django.conf.urls import patterns, url


urlpatterns = patterns('megasena.views',
    url(r'^$', 'home', name='megasena-home'),
    url(r'^detail/(?P<number>\d+)/$', 'detail', name='megasena-detail'),
    url(r'^list/$', 'list', name='megasena-bets-list'),
)
