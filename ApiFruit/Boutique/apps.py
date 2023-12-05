from django.apps import AppConfig


class BoutiqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Boutique'

    def ready(self):
        import Boutique.hooks