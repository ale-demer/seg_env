from django import forms

from .models import VentaNueva


class VentaNuevaForm(forms.ModelForm):
    class Meta:
        model = VentaNueva
        fields = ['client', 'name', 'surname', 'address', 'location', 'service',
                  'payment', 'cash_amount', 'mix_amount', 'only_amount', 'hd_amount']
        labels = {'client': 'Nro de DNI' ,
                  'name': 'Nombre' ,
                  'surname': 'Apellido' ,
                  'address': 'Dirección' ,
                  'location': 'Localidad' ,
                  'service': 'Programación' ,
                  'payment': 'Forma de Pago' ,
                  'cash_amount': 'Importe en $' ,
                  'mix_amount': 'Cant de Mix' ,
                  'only_amount': 'Cant de Only' ,
                  'hd_amount': 'Cant de HD Plus' ,
                  }


class LiquidacionForm(VentaNuevaForm):

    class Meta:
        model = VentaNueva
        fields = ['client', 'name', 'surname', 'address', 'location', 'service',
                  'payment', 'cash_amount', 'mix_amount', 'only_amount', 'hd_amount', 'sds',
                  'payoff', 'status' ]
        labels = {'client': 'Nro de DNI' ,
                  'name': 'Nombre' ,
                  'surname': 'Apellido' ,
                  'address': 'Dirección' ,
                  'location': 'Localidad' ,
                  'service': 'Programación' ,
                  'payment': 'Forma de Pago' ,
                  'cash_amount': 'Importe en $' ,
                  'mix_amount': 'Cant de Mix' ,
                  'only_amount': 'Cant de Only' ,
                  'hd_amount': 'Cant de HD Plus' ,
                  'sds': 'Nro de Cliente' ,
                  'payoff': 'Liquidada' ,
                  'status': 'Estado' ,
                  }
        widgets = {'sds': forms.NumberInput( attrs={'class': 'from-control'}) ,
                   'payoff': forms.CheckboxInput( attrs={'class': 'checkbox', 'data-toggle': "toggle", 'data-on': "Liquidada!",
                                                         'data-off': "No", 'data-onstyle': "success", 'data-offstyle': "danger" } ) ,
                   'status': forms.Select( attrs={'class': 'form-control'} ) ,
                   }