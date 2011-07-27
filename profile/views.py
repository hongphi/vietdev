# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect



@login_required
def profile_home(request):
    '''
    View profile of User.
    @param request:
    '''
    return HttpResponse("Hello world")


@login_required
@csrf_protect
def profile_update(request):
    '''
    Update profile of User.
    @param request:
    '''
    return HttpResponse("Hello world")
