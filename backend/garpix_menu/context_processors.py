"""
Контекстный процессор для меню.
"""
from django.conf import settings
from garpix_menu.models import MenuItem


def check_is_home(url):
    urls = ['', '/']
    for item in settings.LANGUAGES:
        urls.append(f'/{item[0]}')
    return url in urls


def menu_processor(request):
    """
    Контекстный процессор для возможности отображения всех меню на сайте.
    Меню обычно распологаются на нескольких страницах, поэтому вынесено сюда.
    """
    current_path = request.path
    current_path_without_slash = current_path
    if current_path_without_slash[-1] == '/':
        current_path_without_slash = current_path_without_slash[0:-1]

    context = {
        'menus': {}
    }
    for menu_type_arr in settings.CHOICE_MENU_TYPES:
        menu = MenuItem.objects.filter(is_active=True, menu_type=menu_type_arr[0], parent=None)
        context['menus'][menu_type_arr[0]] = menu.order_by('sort', 'title')
        for menu_item in context['menus'][menu_type_arr[0]]:
            if menu_item.get_link() in (current_path, current_path_without_slash):
                menu_item.is_current = True
                menu_item.is_current_full = True
            elif current_path.startswith(menu_item.get_link()):
                if not check_is_home(menu_item.get_link()):
                    menu_item.is_current = True
            elif menu_item.url and menu_item.url.endswith(current_path):
                if not check_is_home(menu_item.get_link()):
                    menu_item.is_current = True
    return context
