from django.conf.urls import include, url, patterns
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from doctor_rj import views

admin.autodiscover()

sitepatters = patterns(
    '',
)

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
)

restpatterns = patterns(
    '',
    url(r'^estabelecimentos$', views.EstabelecimentoList.as_view()),
    url(r'^unidades$', views.EstabelecimentoPorTipoList.as_view()),
    url(r'^estabelecimentos/(?P<pk>[0-9]+)$', views.EstabelecimentoDetail.as_view()),
)

restpatterns = format_suffix_patterns(restpatterns, allowed=['json', 'html', 'xml'])

urlpatterns = sitepatters + urlpatterns + restpatterns
