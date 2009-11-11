from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.conf import settings

from utils import parse_attributes
from forms import BaseRegisterForm


def shib_register(request, RegisterForm=BaseRegisterForm, register_template_name='shibboleth/register.html'):

    attr = parse_attributes(request.META)

    redirect_url = request.REQUEST.get('next', settings.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(attr)
    try:
        user = User.objects.get(username=attr[settings.SHIB_USERNAME])
    except User.DoesNotExist:
        form = RegisterForm()
        context = {'form': form, 'next': redirect_url, 'shib_attrs': attr, }
        return render_to_response(register_template_name, context, context_instance=RequestContext(request))
    except KeyError:
        context = {'shib_attrs': attr, }
        return return render_to_response('shibboleth/attribute_error.html', context, context_instance=RequestContext(request))

    user.set_unusable_password()
    try:
        user.first_name = attr[settings.SHIB_FIRST_NAME]
        user.last_name = attr[settings.SHIB_LAST_NAME]
        user.email = attr[settings.SHIB_EMAIL]
    except:
        pass
    user.save()

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

    if not redirect_url or '//' in redirect_url or ' ' in redirect_url:
        redirect_url = settings.LOGIN_REDIRECT_URL

    return HttpResponseRedirect(redirect_url)
