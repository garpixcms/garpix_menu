from modeltranslation.translator import TranslationOptions, register
from ..models import MenuItem


@register(MenuItem)
class MenuItemTranslationOptions(TranslationOptions):
    fields = ('title', )
