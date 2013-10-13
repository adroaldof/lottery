from django.conf.urls import patterns, url


urlpatterns = patterns('megasena.views',
    url(r'^$', 'home', name='game-home'),
)
