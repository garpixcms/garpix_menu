from django.conf import settings
from django.db import models
from garpix_page.models import BasePage

from garpix_menu.models import MenuItem
from garpix_menu.serializers import MenuItemSerializer


class Page(BasePage):
    content = models.TextField(verbose_name='Содержание', blank=True, default='')

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"
        ordering = ('-created_at',)

    def get_context(self, request=None, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)

        current_path = self.get_absolute_url()

        menus = {}
        menu_items = MenuItem.objects.filter(is_active=True, parent=None).order_by('sort', 'title')
        for menu_type_arr in settings.CHOICE_MENU_TYPES:
            menu_type = menu_type_arr[0]
            menu = list(filter(lambda item: item.menu_type == menu_type, menu_items))
            menus[menu_type] = MenuItemSerializer(menu, context={'request': request, 'current_path': current_path},
                                                  many=True).data
        context.update({
            'menus': menus
        })
        return context

    @classmethod
    def url_patterns(cls):
        patterns = super().url_patterns()
        patterns.update(
            {
                '{model_name}Create': {
                    'verbose_name': 'Создание {model_title}',
                    'pattern': '/create'
                },
                '{model_name}Update': {
                    'verbose_name': 'Редактирование {model_title}',
                    'pattern': '/update/<id>'
                }
            }
        )
        return patterns
