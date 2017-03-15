from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'calc.views.main',),
    # ^ Nada por delante
    # $ Nada por detras
    # ^$ Vacio

    url(r'^(?P<num1>\d{1,9})\+(?P<num2>\d{1,9})', 'calc.views.add',),

    url(r'^(?P<num1>\d{1,9})\-(?P<num2>\d{1,9})', 'calc.views.sub',),

    url(r'^(?P<num1>\d{1,9})\*(?P<num2>\d{1,9})', 'calc.views.mult',),

    url(r'^(?P<num1>\d{1,9})\/(?P<num2>\d{1,9})', 'calc.views.div',),

    #url(r'^admin/', include(admin.site.urls)),

    url(r'^.+', 'calc.views.resourceError',),

)
