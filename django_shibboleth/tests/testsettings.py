# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2011 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
TESTSERVER = 'http://testserver'
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/django-openstack.db',
            },
        }
INSTALLED_APPS = ['django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.sites',
                  'django_shibboleth',
                  'django_shibboleth.tests',
                  'mailer',
                  ]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    )

ROOT_URLCONF = 'django_shibboleth.tests.testurls'
TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'tests', 'templates')
)
SITE_ID = 1
SITE_BRANDING = 'shibboleth'
SITE_NAME = 'shibboleth'

SHIB_ATTRIBUTE_MAP = {
    "HTTP_SHIB_IDENTITY_PROVIDER": (True, "idp"),
    "HTTP_SHIB_SHARED_TOKEN": (True, "shared_token"),
    "HTTP_SHIB_CN": (True, "cn"),
    "HTTP_SHIB_MAIL": (True, "email"),
    "HTTP_SHIB_GIVENNAME": (False, "first_name"),
    "HTTP_SHIB_SN": (False, "last_name"),
}
SHIB_USERNAME = "shared_token"
SHIB_EMAIL = "email"
SHIB_FIRST_NAME = "first_name"
SHIB_LAST_NAME = "last_name"

LOGIN_REDIRECT_URL = "/success"

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--nocapture',
             '--cover-package=django_shibboleth',
             '--cover-inclusive',
            ]

# django-mailer uses a different config attribute
# even though it just wraps django.core.mail
MAILER_EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
EMAIL_BACKEND = MAILER_EMAIL_BACKEND
