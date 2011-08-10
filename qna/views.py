from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.defaultfilters import slugify
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json
from qna.models import Question, Answer
import datetime
from qna.forms import QuestionForm, AnswerForm
from tagging.models import Tag, TaggedItem

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
            question = Question(title = title, content = content, bonus = 0)
            question.author = request.user
            question.save()
            question.tags = tags
            return HttpResponseRedirect('/qna/question/%d/' % question.id)
    else:
        q_form = QuestionForm()
            
    return render_to_response('qna/ask.html',
                              {"form": q_form}, 
                              context_instance = RequestContext(request))
def home_list(request):
    question_list = Question.objects.all().order_by('-date')
    paginator = Paginator(question_list, 10) # 2 questions per page

    questions = paginator.page(1)

    return render_to_response('qna/list.html',
                              {'questions': questions,
                               'user': request.user},
                              context_instance = RequestContext(request))

def list_question(request, page):
    question_list = Question.objects.all().order_by('date')
    paginator = Paginator(question_list, 2) # 2 questions per page
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)
    return render_to_response('qna/list.html',
                              {'questions': questions,
                               'user': request.user},
                              context_instance = RequestContext(request))

def show_question(request, id):
    try:
        question = Question.objects.get(pk = id)
        answers = question.get_answers()
        form = AnswerForm()
        return render_to_response('qna/question.html',
                                  {"question" : question,
                                   "answers": answers,
                                   "form" : form,
                                   "user": request.user},
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


@login_required
def like(request, type, id):
    if type == "question":
        q = Question.objects.get(pk = id)
        q.likes.add(request.user)
        return HttpResponse(q.likes.count())
    elif type == "answer":
        a = Answer.objects.get(pk = id)
        a.likes.add(request.user)
        return HttpResponse(a.likes.count())

@login_required
def unlike(request, type, id):
    if type == "question":
        q = Question.objects.get(pk = id)
        q.likes.remove(request.user)
        return HttpResponse(q.likes.count())
    elif type == "answer":
        a = Answer.objects.get(pk = id)
        a.likes.remove(request.user)
        return HttpResponse(a.likes.count())

def tags_all(request):
    """

    """
    tags = Tag.objects.usage_for_model(Question, counts=True)
    
    type = 'popular'
    if 'sort' in request.GET:
        sort = request.GET['sort']
        if sort == 'name':
            type = 'name'
            tags.sort(cmp = (lambda x, y: cmp(x.name,y.name)), reverse=False)
        else:
            if sort == 'new':
                type = 'new'
                tags.sort(cmp = (lambda x, y: cmp(x.date,y.date)), reverse=True)
    else:
        tags.sort(cmp = (lambda x, y: cmp(x.count,y.count)), reverse=True)

    tags_4 = []
    tags_divide_4 = []
    for i in range(0,tags.__len__(),1):
        tags_4.append(tags[i])
        if i%4==3:
            tags_divide_4.append(tags_4)
            tags_4 = []
    if tags.__len__()%4 != 0:
        tags_divide_4.append(tags_4)
    return render_to_response('qna/tags.html',
                              {"tags": tags_divide_4,
                               "type": type,},
                              context_instance = RequestContext(request))

def question_by_tag(request, name):
    question_list = TaggedItem.objects.get_by_model(Question, name)

    paginator = Paginator(question_list, 10) # 10 questions per page

    questions = paginator.page(1)
    return render_to_response('qna/list.html',
                              {'questions': questions,
                               'user': request.user},
                              context_instance = RequestContext(request))