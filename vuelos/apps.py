from django.apps import AppConfig


class VuelosConfig(AppConfig):
    name = 'vuelos'
    def ready(self):
        import vuelos.signals  # noqa: F401