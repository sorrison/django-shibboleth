from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.conf import settings

from utils import parse_attributes


def shib_register(request, RegisterForm=None, register_template_name='shibboleth/register.html', redirect_url='/profile/'):

    attr = parse_attributes(request.META)
    
    if request.method == 'POST':
        # Post from register_form
        if RegisterForm:
            form = RegisterForm(request.POST)
            if form.is_valid:
                form.save()
        user = User.objects.create_user(attr[settings.SHIB_USERNAME], attr[settings.SHIB_EMAIL], '')

    try:
        user = User.objects.get(username=attr[settings.SHIB_USERNAME])
    except User.DoesNotExist:
        if RegisterForm:
            form = RegisterForm()

        return render_to_response(register_template_name, locals(), context_instance=RequestContext(request))

    user.set_unusable_password()
    user.first_name = attr[settings.SHIB_FIRST_NAME]
    user.last_name = attr[settings.SHIB_LAST_NAME]
    user.email = attr[settings.SHIB_EMAIL]
    user.save()

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

    return HttpResponseRedirect(redirect_url)


