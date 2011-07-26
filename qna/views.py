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

def home(request):
    """
    Just the home page
    """
    return render_to_response('home.html',
        {},
        context_instance = RequestContext(request))

def ask(request):
    if 'q' in request.GET and 't' in request.GET:
        q = request.GET['q']
        t = request.GET['t']
        if q and t:
            question = Question(title = t, content=q)
    return render_to_response('ask.html',{'title' : "",'question' : ""})