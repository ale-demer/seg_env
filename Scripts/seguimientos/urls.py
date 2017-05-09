"""Define URLs para seguimientos."""

from django.conf.urls import url

from . import views

urlpatterns = [
	# Pagina principal.
	url(r'^$', views.index, name='index'),
	
	# Muestra todas las opciones de venta.
	url(r'^ventas/$', views.ventas, name='ventas'),
	
	# Pagina que detalla las ventas cargadas de una determinada categoria.
	url(r'^ventas/(?P<venta_id>\d+)/$', views.venta, name='venta'),
	
	# Pagina para cargar una venta nueva.
	url(r'^venta_nueva/(?P<venta_id>\d+)/$', views.venta_nueva, name='venta_nueva'),
	
	# Pagina para editar una venta ya cargada.
	url(r'^editar_venta/(?P<venta_id>\d+)/$', views.editar_venta, name='editar_venta'),

	# Pagina que detalla las ventas que no estan en estado Finalizada.
	url( r'^venta_caida/(?P<venta_id>\d+)/$', views.venta_caida , name='venta_caida' ) ,

	# Pagina de estadisticas.
	url(r'^stats/$', views.stats, name='stats'),


]