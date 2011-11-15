from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^login$', 'django_shibboleth.views.shib_register',),
)
