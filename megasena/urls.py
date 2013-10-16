from django.conf.urls import patterns, url


urlpatterns = patterns('megasena.views',
    url(r'^$', 'home', name='megasena-home'),
    url(r'^detail/(?P<number>\d+)/$', 'detail', name='megasena-detail'),
    url(r'^add/$', 'add', name='megasena-add-bet'),
    url(r'^bets/$', 'bets', name='megasena-bets-list'),
    url(r'^update/(?P<number>\d+)/$', 'update', name='megasena-update-bet'),
    url(r'^delete/(?P<pk>\d+)/$', 'delete', name='megasena-delete-bet'),
)
