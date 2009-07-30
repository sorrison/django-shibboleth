Introduction
============


Required Settings
=================

 * SHIB_ATTRIBUTE_MAP

Example:

	SHIB_ATTRIBUTE_MAP = {
	    "HTTP_SHIB_IDENTITY_PROVIDER": (True, "idp"),
	    "HTTP_SHIB_SHARED_TOKEN": (True, "shared_token"),
	    "HTTP_SHIB_CN": (True, "cn"),
    	    "HTTP_SHIB_MAIL": (True, "email"),
    	    "HTTP_SHIB_GIVENNAME": (False, "first_name"),
    	    "HTTP_SHIB_SN": (False, "last_name"),
	}


 * SHIB_USERNAME

Example:
	SHIB_USERNAME = "shared_token"


 * SHIB_EMAIL

Example:
	SHIB_EMAIL = "email"

Optional Settings
=================

SHIB_FIRST_NAME
SHIB_LAST_NAME





