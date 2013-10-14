from django.conf.urls import patterns, url


urlpatterns = patterns('parsers.views',
    url(r'^megasena/$', 'parse_megasena', name='parse-megasena'),
    url(r'^parse_file/$', 'parse_file', name='parse-file'),
)