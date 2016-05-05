from django.contrib import admin

from .models import Cuenta

class RegistrarCuenta(admin.ModelAdmin):

	list_display = ["codigocuenta","deposito","fechacreacion","fechatransaccion","llavecuenta","codigocliente"]
	list_display_links = ["codigocuenta","codigocliente"]
	list_filter =["fechacreacion","fechatransaccion"]
	search_fields = ["codigocuenta","deposito","fechacreacion","fechatransaccion","llavecuenta","codigocliente"]

	class Meta:
		model = Cuenta

admin.site.register(Cuenta,RegistrarCuenta)