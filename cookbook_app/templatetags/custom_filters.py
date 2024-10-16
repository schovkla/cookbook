from django import template

register = template.Library


@register.filter
def custom_floatformat(value):
    return "{:.2f}".format(float(value)).rstrip('0').rstrip('.')
