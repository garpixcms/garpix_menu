from django.conf import settings
from django.forms.models import model_to_dict
from garpix_menu.models import MenuItem


def check_is_home(url):
    urls = ['', '/']
    for item in settings.LANGUAGES:
        urls.append(f'/{item[0]}')
    return url in urls


def get_menu_item_dict(menu_item, current_path, current_path_without_slash):
    context = model_to_dict(menu_item)
    link = menu_item.get_link()
    if link in (current_path, current_path_without_slash):
        menu_item.is_current = True
        menu_item.is_current_full = True
    elif current_path.startswith(link):
        if not check_is_home(link):
            menu_item.is_current = True
    elif menu_item.url and menu_item.url.endswith(current_path):
        if not check_is_home(link):
            menu_item.is_current = True

    context['get_link'] = link
    context['is_current'] = menu_item.is_current
    context['is_current_full'] = menu_item.is_current_full
    context['object'] = menu_item
    try:
        context['icon'] = menu_item.icon.url
    except:
        context['icon'] = None

    context.pop('page', None)
    context.pop('title_for_admin', None)

    return context


def get_menus(current_path):
    current_path_without_slash = current_path
    if current_path_without_slash[-1] == '/':
        current_path_without_slash = current_path_without_slash[0:-1]

    menus = {}
    menu_items = MenuItem.on_site.filter(is_active=True, parent=None).order_by('sort', 'title')
    for menu_type_arr in settings.CHOICE_MENU_TYPES:
        menu = list(filter(lambda item: item.menu_type == menu_type_arr[0], menu_items))
        menus[menu_type_arr[0]] = []
        for menu_item in menu:
            menus[menu_type_arr[0]].append(get_menu_item_dict(menu_item, current_path, current_path_without_slash))

    return menus
