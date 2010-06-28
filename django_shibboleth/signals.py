import django.dispatch

shib_logon_done = django.dispatch.Signal(providing_args=["user", "shib_attrs"])
