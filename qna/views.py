from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.defaultfilters import slugify
from django.views.decorators.csrf import csrf_protect

import json
from qna.models import Question, Answer
import datetime
from qna.forms import QuestionForm, AnswerForm


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
            return HttpResponseRedirect('/qna/question/%d/' % question.id)
    else:
        q_form = QuestionForm()
            
    return render_to_response('qna/ask.html',
                              {"form": q_form}, 
                              context_instance = RequestContext(request))

def list_question(request):
    questions = Question.objects.all().order_by('-date')
    return render_to_response('qna/list.html',
                              {'questions': questions},
                              context_instance = RequestContext(request))

def show_question(request, id):
    try:
        question = Question.objects.get(pk = id)
        answers = question.get_answers()
        form = AnswerForm()
        return render_to_response('qna/question.html',
                                  {"question" : question,
                                   "answers": answers,
                                   "form" : form },
                                  context_instance = RequestContext(request))
    except:
        raise Http404()


@csrf_protect
@login_required
def answer(request, id_question):
    if request.method == "POST":
        a_form = AnswerForm(request.POST)
        if a_form.is_valid():
            question = Question.objects.get(pk = id_question)
            content = request.POST["content"]
            ans = Answer(content = content)
            ans.author = request.user
            ans.question = question
            ans.save()
            
    return HttpResponseRedirect('/qna/question/%d/' % int(id_question))
    