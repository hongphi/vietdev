# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



@login_required
def profile_home(request):
    '''
    View profile of User.
    @param request:
    '''
    return HttpResponse("")


@login_required
def profile_update(request):
    '''
    Update profile of User.
    @param request:
    '''
    return HttpResponse("")
