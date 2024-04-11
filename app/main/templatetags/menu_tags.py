from typing import Any, List, Dict

from django import template
from main.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('main/menu.html')
def draw_menu(menu_name: str) -> Dict[str, Any]:
    menu_items = dict()
    menus = Menu.objects.all()
    title_list: List[str] = [menu.title for menu in menus]
    if menu_name in title_list:
        menu_items = MenuItem.objects.filter(parent__title=menu_name)
    return {'menu_items': menu_items, 'menu_name': menu_name, "menus": menus}
