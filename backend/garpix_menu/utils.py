from django.conf import settings
from django.forms.models import model_to_dict


def check_is_home(url):
    urls = ['', '/']
    for item in settings.LANGUAGES:
        urls.append(f'/{item[0]}')
    return url in urls


def get_menu_item_dict(menu_item, current_path):
    context = model_to_dict(menu_item)
    link = menu_item.get_link()

    context['get_link'] = link
    context['is_current'] = menu_item.get_is_current(current_path)
    context['is_current_full'] = menu_item.get_is_current_full(current_path)
    context['object'] = menu_item
    try:
        context['icon'] = menu_item.icon.url
    except Exception:
        context['icon'] = None

    context.pop('page', None)
    context.pop('title_for_admin', None)

    return context


def get_menus(current_path):
    from garpix_menu.models import MenuItem

    menus = {}
    menu_items = MenuItem.on_site.prefetch_related('sites').filter(is_active=True, parent=None).order_by('sort', 'title')
    for menu_type_arr in settings.CHOICE_MENU_TYPES:
        menu = list(filter(lambda item: item.menu_type == menu_type_arr[0], menu_items))
        menus[menu_type_arr[0]] = []
        for menu_item in menu:
            menus[menu_type_arr[0]].append(get_menu_item_dict(menu_item, current_path))

    return menus
