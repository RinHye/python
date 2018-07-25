import re
from django import template
from django.conf import settings

register = template.Library()
numericTest = re.compile("^\d+$")

#Gérer questions random
@register.filter
def lookup(d, key):
	return d[key]

@register.filter
def getAttribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""
    if hasattr(value, str(arg)):
        return getattr(value, arg)
    elif hasattr(value, 'has_key') and value.has_key(arg):
        return value[arg]
    elif numericTest.match(str(arg)) and len(value) > int(arg):
        return value[int(arg)]
    else:
        return settings.TEMPLATES[0]['OPTIONS']['string_if_invalid']

@register.filter
def get(o, index):
    try:
        return o[index]
    except:
        return settings.TEMPLATES[0]['OPTIONS']['string_if_invalid']