# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from profile.models import Profile, Activity
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from profile.forms import ProfileForm



@login_required
def profile_home(request):
    '''
    View profile of User.
    @param request:
    '''
    try:
        profile, created = Profile.objects.get_or_create(user = request.user)
        if created:
            active = Activity(user = request.user)
            active.save()
            return HttpResponseRedirect('/profile/update/')            
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
    if request.method == "POST":
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            title = request.POST['title']
            content = request.POST['content']
            tags = request.POST['tags']
            question = Profile(title = title, content = content, tags = tags, bonus = 0)
            question.author = request.user
            question.save()
    else:
        profile = Profile.objects.get(user = request.user)
        profile_form = ProfileForm(instance = profile)
            
    return render_to_response('profile/update_profile.html',
                              {"form": profile_form}, 
                              context_instance = RequestContext(request))
