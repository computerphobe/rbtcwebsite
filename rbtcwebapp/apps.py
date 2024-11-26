from django.apps import AppConfig


class RbtcwebappConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'rbtcwebapp'
        
    def __str__(self):
        import rbtcwebapp.signals
