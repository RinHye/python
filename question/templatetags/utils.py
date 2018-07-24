from django import template
register = template.Library()

#Gérer questions random
@register.filter
def lookup(d, key):
	print(key)
	return d[key]
