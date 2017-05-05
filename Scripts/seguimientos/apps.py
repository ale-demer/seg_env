from django.apps import AppConfig
from watson import search as watson


class SeguimientosConfig(AppConfig):
    name = 'seguimientos'
    def ready(self):
        VentaNueva = self.get_model("VentaNueva")
        watson.register(VentaNueva)
