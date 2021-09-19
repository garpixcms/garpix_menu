"""
Контекстный процессор для меню.
"""
from .utils import get_menus


def menu_processor(request):
    """
    Контекстный процессор для возможности отображения всех меню на сайте.
    Меню обычно распологаются на нескольких страницах, поэтому вынесено сюда.
    """
    current_path = request.path
    context = {
        'menus': get_menus(current_path),
    }
    return context
