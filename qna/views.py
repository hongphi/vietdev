from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.views.decorators.csrf import csrf_protect

import json


def home(request):
    """
    Just the home page
    """
    return render_to_response('home.html',
        {},
        context_instance = RequestContext(request))
