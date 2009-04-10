from django.conf.urls.defaults import *

# URL patterns for django_shibboleth

urlpatterns = patterns('django_shibboleth.views',
  # Add url patterns here
    url(r'^login/$', 'shib_login', name='shib_login'),
    url(r'^register/$', 'shib_register', name='shib_register'),
)
