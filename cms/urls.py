from django.conf.urls import url
from .views import (
	cmshome,
	listadecuentas,
	cuentas
	)

urlpatterns = [
    url(r'^$', cmshome),
    url(r'^listadecuentas/$', listadecuentas, name="listadecuentas"),
    url(r'^(?P<codigocuenta>\d+)/$', cuentas, name="cuenta"),
]
