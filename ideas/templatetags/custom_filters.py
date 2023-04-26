from django import template
from lib.utils import truncate_text

register = template.Library()

@register.filter(name='truncate_text_filter')
def truncate_text_filter(value, arg):
    try:
        length = int(arg)
    except ValueError:
        return value

    return truncate_text(value, length)



