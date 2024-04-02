from django.apps import AppConfig


class UserCompanyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_company_app'

    def ready(self):
        import user_company_app.signals 