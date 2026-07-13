"""Настройки приложений."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Настройки класса."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
