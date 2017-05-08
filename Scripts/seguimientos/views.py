from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages



from .models import Venta, VentaNueva, User
from .forms import VentaNuevaForm, LiquidacionForm


def index(request):
    """Establece la página principal para Seguimiento."""
    return render(request, 'seguimientos/index.html')


@login_required
def ventas(request):
    """Muestra todos los tipos de venta."""
    ventas = Venta.objects.order_by('date_added')
    context = {'ventas': ventas}
    return render(request, 'seguimientos/ventas.html', context)


@login_required
def venta(request, venta_id):
    """Muestra una categoría de venta y todas las ventas cargadas."""
    venta = get_object_or_404(Venta, id=venta_id)

    try:
        if request.user.groups.filter( name='Liquidaciones' ).exists():
            paginator = Paginator( venta.ventanueva_set.order_by( 'payoff' , '-date_added' ) , 25 )
            page = request.GET.get( 'page' )
            ventas_nuevas = paginator.page( page )
        else:
            paginator = Paginator( venta.ventanueva_set.order_by( 'payoff' , '-date_added' ).filter( owner=request.user ) , 25 )
            page = request.GET.get( 'page' )
            ventas_nuevas = paginator.page( page )
    except PageNotAnInteger:
        # Si la página no es un int, devuelve la primera página.
        ventas_nuevas = paginator.page( 1 )
    except EmptyPage:
        # Si la página esta fuera del rango, devuelve la última página.
        ventas_nuevas = paginator.page( paginator.num_pages )

    context = {'venta': venta , 'ventas_nuevas': ventas_nuevas}
    return render(request, 'seguimientos/venta.html', context)


@login_required
def venta_nueva(request, venta_id):
    """Crea una nueva venta en una categoría determinada."""
    venta = get_object_or_404(Venta, id=venta_id)

    if request.method != 'POST':
        # Si no hay datos cargados, crea un formulario nuevo.
        form = VentaNuevaForm()
        messages.success( request , 'Cliente ingresado satisfactoriamente' )
    else:
        # Hay datos en POST, procesamos el formulario con los datos cargados.
        form = VentaNuevaForm(data=request.POST)
        if form.is_valid():
            venta_nueva = form.save(commit=False)
            venta_nueva.venta = venta
            venta_nueva.owner = request.user
            venta_nueva.save()
            return HttpResponseRedirect(reverse('seguimientos:venta', args=[venta_id]))

    context = {'venta': venta, 'form': form}
    return render(request, 'seguimientos/venta_nueva.html', context)


@login_required
def editar_venta(request, venta_id):
    """Editar una venta cargada recientemente."""
    users = User.objects.all()
    venta_nueva = get_object_or_404(VentaNueva, id=venta_id)
    venta = venta_nueva.venta

    if request.method != 'POST':
        # Crea formulario nuevo.
        form = LiquidacionForm(instance=venta_nueva)
    else:
        # Hay datos en POST, procesamos el formulario con los datos cargados.
        form = LiquidacionForm(instance=venta_nueva, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success( request , 'Datos actualizados' )
            # Si la venta pasa a Liquidada, se le envía un mail al vendedor informandole.
            if form['payoff'].value() == True:
                users.get( id=venta_nueva.owner_id ).email_user( 'Tu venta de ' + venta_nueva.name + ' ' + venta_nueva.surname +
                                                           ' ha sido liquidada!',
                                                           'Email generado automáticamente, no respondas a este correo.',
                                                           from_email='sistema@univisiononline.com.ar' )

            return HttpResponseRedirect(reverse('seguimientos:venta',
                                                args=[venta.id]))


    context = {'venta_nueva': venta_nueva, 'venta': venta, 'form': form}
    return render(request, 'seguimientos/editar_venta.html', context)


@login_required
def stats(request):
    """Establece la página principal para las estadísticas."""
    return render(request, 'seguimientos/stats.html')

