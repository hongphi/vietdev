from django import template
from qna.models import Question, Answer
from profile.models import Profile

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
    if val < 2 or not isinstance(val, int):
        return ""
    else:
        return "s"

@register.filter   
def fullname(obj):
    if isinstance(obj, Profile):
        return obj.get_full_name()
    else:
        return ""

