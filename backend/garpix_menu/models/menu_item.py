from django.db import models
from django.utils import translation
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey
from garpix_page.models import BasePage


class MenuItem(MPTTModel):
    """
    Пункты меню.
    """
    title_for_admin = models.CharField(max_length=100, blank=True, default='', verbose_name='Название для админа')
    title = models.CharField(max_length=100, verbose_name='Название')
    menu_type = models.CharField(default='', max_length=100, choices=settings.CHOICE_MENU_TYPES, verbose_name='Тип меню')
    page = models.ForeignKey(BasePage, null=True, blank=True, verbose_name='Страница, на которую ведет пункт меню', help_text='Если этот пункт не выбран, то будет использовано следующее поле "Внешний URL"', on_delete=models.CASCADE)
    url = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Внешний URL')
    is_active = models.BooleanField(default=True, verbose_name='Включено')
    target_blank = models.BooleanField(default=False, verbose_name='Открывать в новом окне')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    sort = models.IntegerField(default=100, verbose_name='Сортировка', help_text='Чем меньше число, тем выше будет элемент в списке.')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name='Родительский пункт меню', on_delete=models.CASCADE)
    is_current = False
    is_current_full = False

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ('sort', )

    def __str__(self):
        if self.title_for_admin:
            return self.title_for_admin
        return self.title

    def get_link(self):
        if self.page is not None:
            return self.page.get_absolute_url()
        elif self.url is not None or self.url != '':
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

    def get_menu_params(self):
        return settings.MENU_TYPES[self.menu_type]
