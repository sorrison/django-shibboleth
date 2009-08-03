from django import forms
from django.conf import settings
from django.contrib.auth.models import User

class BaseRegisterForm(forms.Form):    

    def save(self, attr):
        user = User.objects.create_user(attr[settings.SHIB_USERNAME], attr[settings.SHIB_EMAIL], '')
        return user
