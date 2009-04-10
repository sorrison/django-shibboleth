# Create your views here.
from django.http import HttpResponseForbidden, HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template import loader

attribute_map = {
"eduPersonAssurance":"HTTP_SHIB_ASSURANCE",
"cn":"HTTP_SHIB_CN",
"givenName":"HTTP_SHIB_GIVENNAME",
"l":"HTTP_SHIB_L",
"mail":"HTTP_SHIB_MAIL",
"o":"HTTP_SHIB_O",
"auEduPersonSharedToken":"HTTP_SHIB_SHARED_TOKEN",
"sn":"HTTP_SHIB_SN",
}


def parse_attributes(request):
    meta = request.META

    attributes = {}
    attributes['idp'] = meta.get('HTTP_SHIB_IDENTITY_PROVIDER')
    attributes['shared_token'] = meta.get(attribute_map['auEduPersonSharedToken'])
    attributes['username'] = meta.get(attribute_map['auEduPersonSharedToken'])
    attributes['email'] = meta.get(attribute_map['mail'])
    attributes['cn'] = meta.get(attribute_map['cn'])
    attributes['organisation'] = meta.get(attribute_map['o'])
    attributes['locality'] = meta.get(attribute_map['l'])
    attributes['first_name'] = meta.get(attribute_map['givenName']) or cn.split(' ')[0]
    attributes['last_name'] = meta.get(attribute_map['sn']) or cn.lstrip(first_name).strip()

    attributes['shared_token'] = 'G_0-_88s1CiUXmJxKPYWF8TugZI'
    attributes['username'] = 'G_0-_88s1CiUXmJxKPYWF8TugZI'
    return attributes


def shib_register(request):

    attrs = parse_attributes(request)
    # TODO Check to see if user already logged in or user already registered

    if attrs['shared_token'] == '' or \
       attrs['email'] == '' or \
       attrs['cn'] == '' or \
       attrs['organisation'] == '' or \
       attrs['locality'] == '':
        return HttpResponseForbidden(loader.render_to_string('forbidden.html', locals(), context_instance=RequestContext(request)))

    try:
        user = User.objects.get(username=attrs['shared_token'])
        return HttpResponseRedirect(reverse('shib_login'))
    except:
        pass

    if request.method == 'POST':
        user = User.objects.create_user(attrs['shared_token'], attrs['email'], '')

        user.set_unusable_password()
        user.first_name = attrs['first_name']
        user.last_name = attrs['last_name']
        user.email = attrs['email']
        user.save()

        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)

        return HttpResponseRedirect(reverse('new_user'))

    return render_to_response('register.html', locals(), context_instance=RequestContext(request))


def shib_login(request):
    attrs = parse_attributes(request)
    # TODO Check to see if user already logged in or user already registered
    #return HttpResponse(str(attrs))

    if attrs['shared_token'] == '' or \
       attrs['email'] == '' or \
       attrs['cn'] == '' or \
       attrs['organisation'] == '' or \
       attrs['locality'] == '':
        return HttpResponseForbidden(loader.render_to_string('forbidden.html', locals(), context_instance=RequestContext(request)))

    try:
        user = User.objects.get(username=attrs['shared_token'])
    except:
        return HttpResponseRedirect(reverse('shib_register'))

    user.set_unusable_password()
    user.first_name = attrs['first_name']
    user.last_name = attrs['last_name']
    user.email = attrs['email']
    user.save()

    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

    return HttpResponseRedirect(reverse('profile'))


