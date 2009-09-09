Introduction
============

This module will register and login users coming from a shibboleth IdP.

To use it you will need to:

   * Add 'django_shibboleth' to your INSTALLED

   * Add to your url scheme:
     	 (r'^shibboleth/', include('django_shibboleth.urls')),
	 

     If you want to override some of the default options you will need to split these urls up.
     You will also need to protect this url location with shibboleth.

     Example in apache would be:

     	     <Location /shibboleth>
	        AuthType shibboleth
        	ShibRequireSession On
        	ShibUseHeaders On
		require valid-user
    	     </Location>


   * Add the required settings (mentioned below)


Views
=====

``django_shibboleth.views.shib_register``
-----------------------------------------

**Description**

Does two things.
 1. For a *new user* it will present a form asking the user to register. 
    Upon submission it will create a ``User`` object and redirect them to settings.LOGIN_REDIRECT_URL.

 2. For an *existing user* it will log the user into the site and also update there details if they have changed from their IdP.
    It will then redirect them to settings.LOGIN_REDIRECT_URL.

**Optional arguments:**

   * ``RegisterForm``: A ``django.forms.Form`` that will be used for registering a user. Must contain a save method that takes in ``shib_attrs``

   * ``register_template_name``: The name of the template used to render the register form.

**Template context:**

The template's context will be:

    * ``form``: The RegisterForm
    
    * ``next``: The url to redirect to after successful submission. If blank settings.LOGIN_REDIRECT_URL will be used.

    * ``shib_attrs``: A dictionary of [shibboleth attribute name]: shibboleth attribute value



Required Settings
=================

SHIB_ATTRIBUTE_MAP
------------------

A dictionary mapping HTTP headers to a tuple.
The tuple contains whether the attribute is required and then the name of the attribute.
    
    Example:

	SHIB_ATTRIBUTE_MAP = {
	    "HTTP_SHIB_IDENTITY_PROVIDER": (True, "idp"),
	    "HTTP_SHIB_SHARED_TOKEN": (True, "shared_token"),
	    "HTTP_SHIB_CN": (True, "cn"),
    	    "HTTP_SHIB_MAIL": (True, "email"),
    	    "HTTP_SHIB_GIVENNAME": (False, "first_name"),
    	    "HTTP_SHIB_SN": (False, "last_name"),
	}


SHIB_USERNAME
-------------

The name of the shibboleth attribute (defined in SHIB_ATTRIBUTE_MAP) that should be used as the username when creating new users from shibboleth.

    Example:
	SHIB_USERNAME = "shared_token"


SHIB_EMAIL
----------

The name of the shibboleth attribute (defined in SHIB_ATTRIBUTE_MAP) that should be used as the email address for users logging on via shibboleth.

    Example:
	SHIB_EMAIL = "email"

Optional Settings
=================

SHIB_FIRST_NAME
---------------

The name of the shibboleth attribute (defined in SHIB_ATTRIBUTE_MAP) that should be used as the first name for users logging on via shibboleth.

    Example:
	SHIB_FIRST_NAME = "first_name"

SHIB_LAST_NAME
--------------

The name of the shibboleth attribute (defined in SHIB_ATTRIBUTE_MAP) that should be used as the last name for users logging on via shibboleth.

    Example:
	SHIB_LAST_NAME = "last_name"





