"""Define URLs para seguimientos."""

from django.conf.urls import url
from django.contrib.auth.views import login, password_change

from . import views

urlpatterns = [	
	# Pagina de inicio de sesión.
	url(r'^login/$', login, {'template_name': 'usuarios/login.html'}, name='login'),
	
	# Pagina de cierre de sesión.
	url(r'^logout/$', views.logout_view, name='logout'),

	# Pagina de cambio de password.
    url( '^change-password/$' , password_change , {'post_change_redirect': 'seguimientos.next_page'} ,
         name='password_change' ) ,

]