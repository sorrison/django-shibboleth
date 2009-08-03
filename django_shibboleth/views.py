from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.conf import settings

from utils import parse_attributes
from forms import BaseRegisterForm

def shib_register(request, RegisterForm=BaseRegisterForm, register_template_name='shibboleth/register.html', redirect_url=settings.LOGIN_REDIRECT_URL):

    attr = parse_attributes(request.META)
    
    if request.REQUEST.has_key('next'):
        redirect_url = request.REQUEST.get('next')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(attr)
    try:
        user = User.objects.get(username=attr[settings.SHIB_USERNAME])
    except User.DoesNotExist:
        form = RegisterForm()
        return render_to_response(register_template_name, locals(), context_instance=RequestContext(request))

    user.set_unusable_password()
    user.first_name = attr[settings.SHIB_FIRST_NAME]
    user.last_name = attr[settings.SHIB_LAST_NAME]
    user.email = attr[settings.SHIB_EMAIL]
    user.save()

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

    if request.REQUEST.has_key('next'):
        redirect_url = request.REQUEST.get('next')

    if not redirect_to or '//' in redirect_to or ' ' in redirect_to:
        redirect_to = settings.LOGIN_REDIRECT_URL

    return HttpResponseRedirect(redirect_url)


