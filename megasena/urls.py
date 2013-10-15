from django.conf.urls import patterns, url


urlpatterns = patterns('megasena.views',
    url(r'^$', 'home', name='megasena-home'),
)
