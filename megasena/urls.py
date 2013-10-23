from django.conf.urls import patterns, url


urlpatterns = patterns(
    'megasena.views',
    url(r'^$', 'home', name='megasena-home'),
    url(r'^detail/(?P<concourse>\d+)/$', 'detail', name='megasena-detail'),
    url(r'^bets/$', 'bets', name='megasena-bets-list'),
    url(r'^create/$', 'create', name='megasena-create-bet'),
    url(r'^update/(?P<concourse>\d+)/$', 'update', name='megasena-update-bet'),
    url(r'^delete/(?P<pk>\d+)/$', 'delete', name='megasena-delete-bet'),
    url(r'^check/(?P<concourse>\d+)', 'check', name='megasena-check-bet'),
    url(r'^check/all', 'check_all', name='megasena-check-all'),
)
