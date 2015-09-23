from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    # Examples:

    # url(r'^$', 'project_x.views.home', name='home'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^$','home.views.index'),

    url(r'^home$', 'home.views.homepage'),

    url(r'^login$','logins.views.login_user'),

    url(r'^logout$','logins.views.logout_user'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^register/', 'registration.views.register'),

    url(r'^company/(?P<comp_name>\w+)$','home.views.company'),

    url(r'^stats/(?P<c_name>\w+)$','statistics.views.stats')

)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    )
