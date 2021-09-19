from django.conf import settings
from django.forms.models import model_to_dict
from garpix_menu.models import MenuItem


def check_is_home(url):
    urls = ['', '/']
    for item in settings.LANGUAGES:
        urls.append(f'/{item[0]}')
    return url in urls


def get_menus(current_path):
    current_path_without_slash = current_path
    if current_path_without_slash[-1] == '/':
        current_path_without_slash = current_path_without_slash[0:-1]

    menus = {}
    for menu_type_arr in settings.CHOICE_MENU_TYPES:
        menu = MenuItem.objects.filter(is_active=True, menu_type=menu_type_arr[0], parent=None)
        menus[menu_type_arr[0]] = []
        for menu_item in menu.order_by('sort', 'title'):
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
            menus[menu_type_arr[0]].append(model_to_dict(menu_item))
            menus[menu_type_arr[0]][-1]['get_link'] = link
            menus[menu_type_arr[0]][-1]['is_current'] = menu_item.is_current
            menus[menu_type_arr[0]][-1]['is_current_full'] = menu_item.is_current_full
            menus[menu_type_arr[0]][-1].pop('page', None)
            menus[menu_type_arr[0]][-1].pop('title_for_admin', None)
    return menus
