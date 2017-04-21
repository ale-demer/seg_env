from django.db import models
from django.contrib.auth.models import User


class Venta(models.Model):
    """Carga el tipo de venta."""
    text = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Devuelve una representacion textual del modelo."""
        return self.text


class VentaNueva(models.Model):
    """Datos especificos para la carga de una nueva venta."""
    venta = models.ForeignKey(Venta)
    date_added = models.DateTimeField(auto_now_add=True)
    client = models.IntegerField(unique=True)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    # Describimos los tipos de programacion para el dropdown list y los puntos que asigna.
    PREPAGO = 2
    PLATA = 3
    ORO = 4
    OROHD = 5
    HDPLUS = 10
    PLATINO = 10
    NEXUS = 10
    SERVICE_CHOICES = (
        (PREPAGO, 'Prepago'),
        (PLATA, 'Plata'),
        (ORO, 'Oro'),
        (OROHD, 'Oro HD'),
        (HDPLUS, 'Oro HD Plus'),
        (PLATINO, 'Platino'),
        (NEXUS, 'Nexus'),
    )
    service = models.IntegerField(choices=SERVICE_CHOICES, default=OROHD)
    payment = models.IntegerField(choices=((0, 'TC'), (1, 'Efectivo')), default=0)
    cash_amount = models.IntegerField(default=0)
    mix_amount = models.IntegerField(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')), default=0)
    only_amount = models.IntegerField(choices=((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')), default=0)
    hd_amount = models.IntegerField(choices=((0, '0'), (1, '1')), default=0)

    # Setea el usuario como dueño de la venta.
    owner = models.ForeignKey(User)

    # Campos exclusivos para el grupo Liquidaciones.
    paid = models.NullBooleanField()
    payoff = models.BooleanField(default=False)
    sds = models.IntegerField(default=0)

    # Describimos los tipos de estado posibles.
    FI = 'Finalizada'
    VC = 'Venta Caída'
    RE = 'Rechazada'
    PR = 'Prospect'
    PE = 'Pendiente'
    STATUS_CHOICES = (
        (FI, 'Finalizada'),
        (VC, 'Venta Caída'),
        (RE, 'Rechazada'),
        (PR, 'Prospect'),
        (PE, 'Pendiente'),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=12, default=FI)

    class Meta:
        verbose_name_plural = 'ventas nuevas'


    def __str__(self):
        """Devuelve una representacion textual del modelo."""
        return "DNI: " + str(self.client) + " - " + self.surname + " de " + self.location
