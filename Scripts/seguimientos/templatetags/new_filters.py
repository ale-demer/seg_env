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
    if current_month == '01':
        current_month = '13'
    ventas = VentaNueva.objects.filter( date_added__month=int(current_month) -1 )
    i = 0
    for venta in ventas:
        i += 1
    return i


@register.filter( name='total_daily_sales' )
def total_daily_sales(user):
    """Cuenta cantidad de ventas diarias por grupo."""
    mydate = datetime.datetime.now()
    current_day = mydate.strftime( "%d" )
    sale_locations = {"IRS0400": 0, "IRS0401": 0, "IRS0402": 0, "IRS0403": 0, "IRS0405": 0, "IRS0406": 0}
    for loc in sale_locations.keys():
        ventas = VentaNueva.objects.filter( date_added__day=current_day, owner__groups__name=str(loc) )
        i = 0
        for venta in ventas:
            i += 1
            sale_locations[str(loc)] = i

    """ Arma una lista [group / amount] para que se visualize en el graph. """
    list_full = []
    list_full.append( ["Oficina" , "Cantidad de Ventas"] )

    for [k, v] in sale_locations.items():
        list_full.extend([[k, v]])

    return list(list_full)

