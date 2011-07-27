# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from profile.models import Profile



@login_required
def profile_home(request):
    '''
    View profile of User.
    @param request:
    '''
    try:
        profile = Profile.objects.get_or_create()
    except Exception as e:
        pass
    return HttpResponse("Hello world")


@login_required
@csrf_protect
def profile_update(request):
    '''
    Update profile of User.
    @param request:
    '''
    return HttpResponse("Hello world")
