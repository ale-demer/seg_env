from django import template

from seguimientos.models import VentaNueva, User

import datetime
from calendar import monthrange

register = template.Library()


@register.filter( name='has_group' )
def has_group(user , group_name):
    return user.groups.filter( name=group_name ).exists()


@register.filter( name='points_sum' )
def points_sum(user):
    """Suma los puntos del vendedor para el mes en curso."""
    mydate = datetime.datetime.now()
    current_month = mydate.strftime( "%m" )
    current_year = mydate.strftime( "%Y" )
    ventas = VentaNueva.objects.filter( owner=user.id, payoff_date__month=current_month, date_added__year=current_year )
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
    current_year = mydate.strftime( "%Y" )
    ventas = VentaNueva.objects.filter( date_added__month=current_month, date_added__year=current_year )
    i = 0
    for venta in ventas:
        i += 1
    return i


@register.filter( name='last_month_sales' )
def last_month_sales(user):
    """Cuenta la cantidad total de ventas en el mes anterior."""
    mydate = datetime.datetime.now()
    current_month = mydate.strftime( "%m" )
    current_year = mydate.strftime( "%Y" )
    if current_month == '01':
        current_month = '13'
        current_year = int(current_year) - 1
    ventas = VentaNueva.objects.filter( date_added__month=int(current_month) -1, date_added__year=current_year )
    i = 0
    for venta in ventas:
        i += 1
    return i


@register.filter( name='total_daily_sales' )
def total_daily_sales(user):
    """Cuenta cantidad de ventas diarias POR GRUPO."""
    mydate = datetime.datetime.now()
    current_day = mydate.strftime( "%d" )
    current_month = mydate.strftime( "%m" )
    current_year = mydate.strftime( "%Y" )
    sale_locations = {"IRS0400": 0, "IRS0401": 0, "IRS0402": 0, "IRS0403": 0, "IRS0405": 0, "IRS0406": 0}
    for loc in sale_locations.keys():
        ventas = VentaNueva.objects.filter( date_added__day=current_day, date_added__month=current_month,
                                                date_added__year=current_year, owner__groups__name=str(loc) )
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


@register.filter( name='total_daily_sales_by_vendor' )
def total_daily_sales_by_vendor(user):
    """Cuenta cantidad de ventas diarias POR VENDEDOR."""
    mydate = datetime.datetime.now()
    current_day = mydate.strftime( "%d" )
    current_month = mydate.strftime( "%m" )
    current_year = mydate.strftime( "%Y" )
    vendor_name = []
    vendor_name.append( ["Vendedor" , "Cantidad"] )
    users = User.objects.all().exclude(groups__name="Liquidaciones")
    for user in users:
        vendor_name.append( [user.username , 0] )

    for v in range(len(vendor_name)):
        for vendor in vendor_name[v]:
            ventas = VentaNueva.objects.filter( date_added__day=current_day, date_added__month=current_month,
                                                date_added__year=current_year, owner__username=vendor )
            i = 0
            for venta in ventas:
                i += 1
                vendor_name[v][1] = i

    return vendor_name


@register.filter( name='total_daily_sales_per_month' )
def total_daily_sales_per_month(user):
    """Cuenta cantidad de ventas de cada día del mes en curso."""
    mydate = datetime.datetime.now()
    current_month = mydate.strftime( "%m" )
    current_year = mydate.strftime( "%Y" )
    days_amount = monthrange(int(current_year), int(current_month))[1]
    days_list = []

    for i in range(days_amount + 1):
        days_list.append( [i, 0] )

    for d in range(len(days_list)):
        for day in days_list[d]:
            ventas = VentaNueva.objects.filter( date_added__day=str(d), date_added__month=current_month,
                                                date_added__year=current_year)
            i = 0
            for venta in ventas:
                i += 1
                days_list[d][1] = i

    days_list.remove([0, 0])
    days_list.insert( 0, ["Día" , "Cantidad"] )
    return days_list