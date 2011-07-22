from django import template

register = template.Library()

@register.filter
def test(value, agr):
    return value + agr

