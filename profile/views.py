# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_protect
from profile.models import Profile
from django.shortcuts import render_to_response
from django.template.context import RequestContext



@login_required
def profile_home(request):
    '''
    View profile of User.
    @param request:
    '''
    try:
        profile = Profile.objects.get_or_create(user = request.user)
    except Exception as e:
        raise Http404()
    
    return render_to_response('profile/profile.html', {'profile' : profile},
                              context_instance = RequestContext(request))


@login_required
@csrf_protect
def profile_update(request):
    '''
    Update profile of User.
    @param request:
    '''
    return HttpResponse("Hello world")
