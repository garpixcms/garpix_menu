from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings


def validate_type(value):
    exp = value.name.rsplit('.')[-1]
    if exp not in settings.MENU_ICON_ALLOWED_TYPES:
        alowed_types_str = ', '.join(settings.MENU_ICON_ALLOWED_TYPES)
        raise ValidationError(
            _('Допустимые типы') + " - " + alowed_types_str,
            params={'value': value},
        )


def validate_size(value):
    max_size = settings.MENU_ICON_MAX_SIZE / 1024 / 1024
    print(settings.MENU_ICON_MAX_SIZE, max_size, value.size)
    if value.size > settings.MENU_ICON_MAX_SIZE:
        raise ValidationError(
            _(f'Допустимый размер не более {max_size} МБ'),
            params={'value': value},
        )
