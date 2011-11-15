from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^login$', 'django_shibboleth.views.shib_register',),
    url(r'^success$', 'django_shibboleth.tests.testviews.success',),
)
