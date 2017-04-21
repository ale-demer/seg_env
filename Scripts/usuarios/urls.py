"""Define URLs para seguimientos."""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [	
	# Pagina de inicio de sesión.
	url(r'^login/$', login, {'template_name': 'usuarios/login.html'}, name='login'),
	
	# Pagina de cierre de sesión.
	url(r'^logout/$', views.logout_view, name='logout'),

]