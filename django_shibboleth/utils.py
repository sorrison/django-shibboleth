from django.conf import settings
from django.http import HttpResponseForbidden


def parse_attributes(META):
    shib_attrs = {}

    for header, attr in settings.SHIB_ATTRIBUTE_MAP.items():
        required, name = attr
        a = META.get(header, None)
        shib_attrs[name] = a

        if required and not a:
            return HttpResponseForbidden("Required attribute %s not found" % name)

    return shib_attrs
