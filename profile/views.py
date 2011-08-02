# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from profile.models import Profile, Activity
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from profile.forms import ProfileForm
from django.contrib.auth.models import User



@login_required
def profile_home(request):
    '''
    View profile of User.
    @param request:
    '''
    return HttpResponseRedirect('/profile/' + request.user.username)

@login_required
def view_profile(request, username):
    try:
        required_user = User.objects.get(username = username)
        profile, created = Profile.objects.get_or_create(user = required_user)
        if created:
            active = Activity(user = required_user)
            active.save()
            if required_user == request.user:
                return HttpResponseRedirect('/profile/update/')
                        
    except Exception as e:
        raise Http404()
    
    return render_to_response('profile/profile.html', {'profile' : profile},
                              context_instance = RequestContext(request))


@login_required
@csrf_protect
def profile_update(request, username):
    '''
    Update profile of User.
    @param request:
    '''
    profile, created = Profile.objects.get_or_create(user = request.user)
    if created:
        active = Activity(user = request.user)
        active.save()

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance = profile)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect('/profile/' + username)
    else:        
        profile_form = ProfileForm(instance = profile)
            
    return render_to_response('profile/update_profile.html',
                              {"form": profile_form}, 
                              context_instance = RequestContext(request))
