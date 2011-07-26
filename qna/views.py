from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.views.decorators.csrf import csrf_protect

import json
from qna.models import Question
import datetime
from qna.forms import QuestionForm


def home(request):
    """
    Just the home page
    """
    return render_to_response('home.html',
        {},
        context_instance = RequestContext(request))

@login_required
@csrf_protect
def ask(request):    
    if request.method == "POST":
        q_form = QuestionForm(request.POST)
        if q_form.is_valid():
            title = request.POST['title']
            content = request.POST['content']
            tags = request.POST['tags']
            question = Question(title = title, content = content, tags = tags, bonus = 0)
            question.author = request.user
            question.save()
            q_form = QuestionForm()
    else:
        q_form = QuestionForm()
            
    return render_to_response('ask.html',{"form" : q_form}, context_instance = RequestContext(request))



