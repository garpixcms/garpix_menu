from django.db import models
from django.utils import translation
from django.conf import settings
from garpix_page.models import BasePage
from garpix_utils.file import get_file_path


class LinkMixin(models.Model):
    """
    Пункты меню.
    """
    page = models.ForeignKey(BasePage, null=True, blank=True, verbose_name='Страница, на которую ведет пункт меню', help_text='Если этот пункт не выбран, то будет использовано следующее поле "Внешний URL"', on_delete=models.CASCADE)
    subpage_url = models.CharField(max_length=256, null=True, blank=True, verbose_name='URL подстраницы (при наличии)')
    url = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Внешний URL')
    hash = models.CharField(max_length=256, default='', blank=True, verbose_name='Якорь', help_text='Если хотите дать ссылку на конкретный элемент страницы. Например - #example')
    file = models.FileField(upload_to=get_file_path, blank=True, null=True, verbose_name='Файл')

    class Meta:
        abstract = True

    def get_link(self, request=None):
        if self.file not in (None, ''):
            if request:
                return request.build_absolute_uri(self.file.url)
            return self.file.url
        elif self.page is not None:
            subpage_url = self.subpage_url if self.subpage_url else ''
            return f"{self.page.get_absolute_url()}{subpage_url}{self.hash}"
        elif self.url is not None and self.url != '':
            if self.url.startswith('/'):
                current_language_code_url_prefix = translation.get_language()
                if current_language_code_url_prefix == settings.LANGUAGE_CODE:
                    return "{}{}".format(self.url, self.hash)
                return "/{}{}{}".format(current_language_code_url_prefix, self.url, self.hash)
            else:
                return self.url
        elif self.hash is not None and self.hash != '':
            return self.hash
        else:
            return '#'
    get_link.short_description = 'URL'
