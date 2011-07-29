from django import template
from qna.models import Question, Answer

register = template.Library()

@register.filter
def test(value, agr):
    return value + agr

@register.filter
def count_answer(obj):
    if isinstance(obj, Question):
        return Answer.objects.filter(question = obj).count()
    else:    
        raise TypeError("Object input must be a instance of Question!")
    
    
@register.filter
def pluralize(val):
    if val < 2:
        return ""
    else:
        return "s"

