from django.contrib.sites.models import Site
from django.db import models
from django.conf import settings
from garpix_page.utils.all_sites import get_all_sites
from garpix_utils.file import get_file_path
from mptt.models import MPTTModel, TreeForeignKey
from garpix_utils.managers import ActiveManager
from ..mixins import LinkMixin
from ..utils import check_is_home
from ..validators import validate_type, validate_size
from garpix_utils.managers import GCurrentSiteManager


class MenuItem(LinkMixin, MPTTModel):
    """
    Пункты меню.
    """
    title_for_admin = models.CharField(max_length=100, blank=True, default='', verbose_name='Название для админа')
    title = models.CharField(max_length=100, verbose_name='Название')
    icon = models.FileField(
        upload_to=get_file_path, verbose_name='Иконка', blank=True, null=True,
        validators=[validate_type, validate_size]
    )
    menu_type = models.CharField(default='', max_length=100, choices=settings.CHOICE_MENU_TYPES, verbose_name='Тип меню')
    is_active = models.BooleanField(default=True, verbose_name='Включено')
    target_blank = models.BooleanField(default=False, verbose_name='Открывать в новом окне')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    sort = models.IntegerField(default=100, verbose_name='Сортировка', help_text='Чем меньше число, тем выше будет элемент в списке.')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, verbose_name='Родительский пункт меню', on_delete=models.CASCADE)
    sites = models.ManyToManyField(Site, default=get_all_sites, verbose_name='Сайты для отображения')
    is_current = False
    is_current_full = False
    active_manager = ActiveManager()
    on_site = GCurrentSiteManager()

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ('sort', )
        abstract = False

    def __str__(self):
        if self.title_for_admin:
            return self.title_for_admin
        return self.title

    def get_menu_params(self):
        return settings.MENU_TYPES[self.menu_type]

    def get_active_children(self):
        return MenuItem.on_site.filter(parent=self, is_active=True)

    def get_is_current(self, current_path):

        link = self.get_link()

        current_path_without_slash = current_path
        if current_path_without_slash[-1] == '/':
            current_path_without_slash = current_path_without_slash[0:-1]

        if link in (current_path, current_path_without_slash):
            return True
        elif current_path.startswith(link):
            if not check_is_home(link):
                return True
        elif self.url and self.url.endswith(current_path):
            if not check_is_home(link):
                return True

        return False

    def get_is_current_full(self, current_path):

        current_path_without_slash = current_path
        if current_path_without_slash[-1] == '/':
            current_path_without_slash = current_path_without_slash[0:-1]

        return self.get_link() in (current_path, current_path_without_slash)
