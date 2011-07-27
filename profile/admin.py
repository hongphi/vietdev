from django.contrib import admin
from profile.models import Profile, Experience


class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'gender', 'birthday', 'joined_date']
    list_filter = ('user__username', 'joined_date',)
    search_fields = ('user__username, joined_date','gender')
  
admin.site.register(Profile, AdminProfile)

class AdminExperience(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'technical_use', 'work_time']
    list_filter = ('user__username', 'company_name',)
    search_fields = ('user__username', 'company_name','technical_use', 'work_time')
    
admin.site.register(Experience, AdminExperience)