from django.conf import settings
from django.db import models
from garpix_page.models import BasePage


class Page(BasePage):
    content = models.TextField(verbose_name='Содержание', blank=True, default='')

    page_types = [settings.PAGE_TYPE_HOME, settings.PAGE_TYPE_DEFAULT]

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
        ordering = ('-created_at',)
