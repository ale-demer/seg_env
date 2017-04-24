from django import template

from seguimientos.models import VentaNueva

import datetime

register = template.Library()


@register.filter( name='has_group' )
def has_group(user , group_name):
    return user.groups.filter( name=group_name ).exists()


@register.filter( name='points_sum' )
def points_sum(user):
    """Suma los puntos del vendedor para el mes en curso."""
    mydate = datetime.datetime.now()
    current_month = mydate.strftime( "%m" )
    ventas = VentaNueva.objects.filter( owner=user.id, date_added__month=current_month )
    i = 0
    for venta in ventas:
        if venta.payoff == True and venta.status in ('Finalizada', 'OK'):
            i += venta.service
    return i


@register.filter( name='sale_by_group_400' )
def sale_by_group_400(user):
    """Cuenta cantidad de ventas diarias por grupo."""
    mydate = datetime.datetime.now()
    current_day = mydate.strftime( "%d" )
    ventas = VentaNueva.objects.filter( date_added__day=current_day, owner__groups=3 )
    i = 0
    for venta in ventas:
        i += 1
    return i


@register.filter( name='sale_by_group_401' )
def sale_by_group_401(user):
    """Cuenta cantidad de ventas diarias por grupo."""
    mydate = datetime.datetime.now()
    current_day = mydate.strftime( "%d" )
    ventas = VentaNueva.objects.filter( date_added__day=current_day, owner__groups=4 )
    i = 0
    for venta in ventas:
        i += 1
    return i


@register.filter( name='sale_by_group_402' )
def sale_by_group_402(user):
    """Cuenta cantidad de ventas diarias por grupo."""
    mydate = datetime.datetime.now()
    current_day = mydate.strftime( "%d" )
    ventas = VentaNueva.objects.filter( date_added__day=current_day, owner__groups=5 ) # <-- Need to fix this.
    i = 0
    for venta in ventas:
        i += 1
    return i


@register.filter( name='sale_by_group_403' )
def sale_by_group_403(user):
    """Cuenta cantidad de ventas diarias por grupo."""
    mydate = datetime.datetime.now()
    current_day = mydate.strftime( "%d" )
    ventas = VentaNueva.objects.filter( date_added__day=current_day, owner__groups=6 )
    i = 0
    for venta in ventas:
        i += 1
    return i


@register.filter( name='sale_by_group_405' )
def sale_by_group_405(user):
    """Cuenta cantidad de ventas diarias por grupo."""
    mydate = datetime.datetime.now()
    current_day = mydate.strftime( "%d" )
    ventas = VentaNueva.objects.filter( date_added__day=current_day, owner__groups=7 )
    i = 0
    for venta in ventas:
        i += 1
    return i


@register.filter( name='sale_by_group_406' )
def sale_by_group_406(user):
    """Cuenta cantidad de ventas diarias por grupo."""
    mydate = datetime.datetime.now()
    current_day = mydate.strftime( "%d" )
    ventas = VentaNueva.objects.filter( date_added__day=current_day, owner__groups=8 )
    i = 0
    for venta in ventas:
        i += 1
    return i


@register.filter( name='monthly_sales' )
def monthly_sales(user):
    """Cuenta la cantidad total de ventas en el mes actual."""
    mydate = datetime.datetime.now()
    current_month = mydate.strftime( "%m" )
    ventas = VentaNueva.objects.filter( date_added__month=current_month )
    i = 0
    for venta in ventas:
        i += 1
    return i


@register.filter( name='last_month_sales' )
def last_month_sales(user):
    """Cuenta la cantidad total de ventas en el mes anterior."""
    mydate = datetime.datetime.now()
    current_month = mydate.strftime( "%m" )
    ventas = VentaNueva.objects.filter( date_added__month=int(current_month) -1 )
    i = 0
    for venta in ventas:
        i += 1
    return i