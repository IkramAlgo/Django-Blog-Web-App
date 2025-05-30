from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    
    def ready(self):
        import user.signals  # Import the signals module to ensure signals are registered

# This ensures that the signals are connected when the app is ready
# and the app is loaded.