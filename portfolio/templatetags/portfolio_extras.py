from django import template

register = template.Library()

@register.filter
def split(value, arg):
    if not value:
        return []
    return value.split(arg)
