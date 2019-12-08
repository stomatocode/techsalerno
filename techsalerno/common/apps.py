from django.apps import AppConfig


class CommonAppConfig(AppConfig):
    name = "techsalerno.common"
    verbose_name = "Common"

    def ready(self):
        """Override this to put in:
            Common system checks
            common signal registration
        """
        try:
            import techsalerno.common.signals  # noqa F401
        except ImportError:
            pass
