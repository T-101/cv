from django import template

from django.conf import settings

register = template.Library()


@register.filter
def lol_crypt(value, arg):
    translation = value.maketrans(settings.CHAR_SET, arg)
    return value.translate(translation)
