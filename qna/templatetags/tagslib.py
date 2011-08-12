from django import template
from qna.models import Question, Answer
from profile.models import Profile
from tagging.models import Tag, TaggedItem
import datetime

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

@register.filter
def already_like(obj, user):
    if isinstance(obj, Question) or isinstance(obj, Answer):
        if user in obj.likes.all():
            return "unlike"
        else:
            return "like"
    else:
        raise TypeError("Object input must be a instance of Question or Answer!")

@register.filter
def in_24h(obj):
    if isinstance(obj, Tag):
        questions = TaggedItem.objects.get_by_model(Question, obj.name)
        return questions.filter(date = datetime.date.today()).count()
    else:
        raise TypeError("Object input must be a instance of Tag!")

@register.filter
def in_week(obj):
    if isinstance(obj, Tag):
        questions = TaggedItem.objects.get_by_model(Question, obj.name)
        count = 0
        for q in questions:
            if q.date.day > datetime.date.today().day - 7:
                count += 1
        return count
    else:
        raise TypeError("Object input must be a instance of Tag!")
