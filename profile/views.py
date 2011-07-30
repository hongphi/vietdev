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
            first_name   = request.POST['first_name'] 
            middle_name  = request.POST['middle_name']
            last_name    = request.POST['last_name']
            website      = request.POST['website']
            birthday     = request.POST['birthday']
            home_address = request.POST['home_address']
            work_address = request.POST['work_address']
            gender       = request.POST['gender']
            education    = request.POST['education']
            avatar       = request.POST['avatar']
            about_user   = request.POST['about_user']
            home_phone   = request.POST['home_phone']
            work_phone   = request.POST['work_phone']
            mobile_phone = request.POST['mobile_phone']
            interests    = request.POST['interests']
            profile = Profile.objects.get(user = request.user)
            profile.first_name   = first_name   
            profile.middle_name  = middle_name 
            profile.last_name    = last_name   
            profile.website      = website     
            profile.birthday     = birthday    
            profile.home_address = home_address
            profile.work_address = work_address
            profile.gender       = gender      
            profile.education    = education   
            profile.avatar       = avatar      
            profile.about_user   = about_user  
            profile.home_phone   = home_phone  
            profile.work_phone   = work_phone  
            profile.mobile_phone = mobile_phone
            profile.interests    = interests
            profile.save()    
                                 
    else:
        profile = Profile.objects.get(user = request.user)
        profile_form = ProfileForm(instance = profile)
            
    return render_to_response('profile/update_profile.html',
                              {"form": profile_form}, 
                              context_instance = RequestContext(request))
