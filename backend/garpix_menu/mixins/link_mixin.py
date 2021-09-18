from django.db import models
from django.utils import translation
from django.conf import settings
from garpix_page.models import BasePage


class LinkMixin(models.Model):
    """
    Пункты меню.
    """
    page = models.ForeignKey(BasePage, null=True, blank=True, verbose_name='Страница, на которую ведет пункт меню', help_text='Если этот пункт не выбран, то будет использовано следующее поле "Внешний URL"', on_delete=models.CASCADE)
    url = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Внешний URL')

    class Meta:
        abstract = True

    def get_link(self):
        if self.page is not None:
            return self.page.get_absolute_url()
        elif self.url is not None and self.url != '':
            if self.url.startswith('/'):
                current_language_code_url_prefix = translation.get_language()
                if current_language_code_url_prefix == settings.LANGUAGE_CODE:
                    return "{}".format(self.url)
                return "/{}{}".format(current_language_code_url_prefix, self.url)
            else:
                return self.url
        else:
            return '#'
    get_link.short_description = 'URL'
