from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)


class CoreConfig(AppConfig):
    name = 'hrm.core'
    verbose_name = "eHRM core app config"

    def ready(self):
        logger.info("eHRM core app ready!")
