'''
Created on Jun 4, 2011

@author: hongphi
'''
from django import template

register = template.Library()

@register.filter
def test(value, agr):
    return value + agr

