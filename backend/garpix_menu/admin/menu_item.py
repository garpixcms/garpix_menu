from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from mptt.admin import DraggableMPTTAdmin
from garpix_menu.models import MenuItem
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(MenuItem)
class MenuItemAdmin(TabbedTranslationAdmin, DraggableMPTTAdmin):
    actions = ('rebuild',)
    list_filter = ('parent', 'is_active')
    list_display = ('tree_actions', 'indented_title', 'title', 'menu_type', 'get_link', 'target_blank', 'is_active', 'sort')
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    search_fields = ('title',)
    list_editable = ('sort',)
    list_display_links = ('indented_title',)

    def _rebuild(self):
        try:
            self.model.objects.rebuild()
        except:  # noqa
            pass

    def rebuild(self, request, queryset):
        """
        Пересорбать МПТТ модель. Иногда требуется для перезагрузки дерева.
        """
        self._rebuild()
    rebuild.short_description = 'Пересобрать пункты раздела'

    def save_model(self, request, obj, form, change):
        # пересобрать МПТТ объекты
        self._rebuild()
        super().save_model(request, obj, form, change)
