from django import template
from qna.models import Question, Answer
from profile.models import Profile

register = template.Library()

@register.filter
def no_answer(val):
    if val < 1 or not isinstance(val, int):
        return "no_answer"
    else:
        return "answers"

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

@register.filter
def count_like(obj):
    if isinstance(obj, Question) or isinstance(obj, Answer):
        return obj.likes.count()
    else:
        raise TypeError("Object input must be a instance of Question or Answer!")