from django.conf.urls import url
from .views import (
	mainhome,
	)

urlpatterns = [
    url(r'^$', mainhome),
]
