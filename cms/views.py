from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Cuenta

def cmshome(request):
	return render(request,"cmshome.html",{})
	
def listadecuentas(request):
	if request.user.is_authenticated():
		query = Cuenta.objects.all()
		contexto = {
			"lista": query,
			"titulo": "Lista de Cuentas",
			"detalle": "Logged in!! :)"
		}
	else:
		contexto = {
			"titulo": "Lista de Cuentas No",
			"detalle": "por favor login :("
	}
	return render(request,"cmscuentas.html",contexto)

def cuentas(request,codigocuenta):
	if request.user.is_authenticated():
		instance = get_object_or_404(Cuenta,codigocuenta=codigocuenta)
		contexto = {
			"titulo": instance.codigocuenta,
			"detalle": "Logged in!! :)",
			"instancia": instance,
		}
	else:
		contexto = {
			"titulo": "Lista de Cuentas No",
			"detalle": "por favor login :("
	}
	return render(request,"cmscuentasunicas.html",contexto)