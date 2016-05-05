from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.conf import settings

class Cuenta(models.Model):
    
    codigocuenta = models.AutoField(primary_key=True,null=False)
    llavecuenta =  models.CharField(max_length=128)
    codigocliente = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    deposito = models.IntegerField(null=False)
    fechacreacion = models.DateTimeField(auto_now=False,auto_now_add=True)
    fechatransaccion = models.DateTimeField(auto_now=False,auto_now_add=True)


    def __unicode__(self):
        return self.llavecuenta

    def __str__(self):
        return self.llavecuenta