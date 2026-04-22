from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """Split a string by the given argument"""
    if not value:
        return []
    return value.split(arg)
