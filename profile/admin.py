from django.contrib import admin
from profile.models import Profile, Experience, Activity


class AdminProfile(admin.ModelAdmin):
    order_by = ['user__username']
    list_display = ['user', 'gender', 'birthday', 'joined_date']
    list_filter = ('user__username', 'joined_date',)
    search_fields = ('user__username, joined_date','gender')
  
admin.site.register(Profile, AdminProfile)

class AdminExperience(admin.ModelAdmin):
    order_by = ['user__username']
    list_display = ['user', 'position','company_name', 'technical_use', 'work_time']
    list_filter = ('user__username', 'company_name',)
    search_fields = ('user__username', 'position','company_name','technical_use', 'work_time')
    
admin.site.register(Experience, AdminExperience)

class AdminActivity(admin.ModelAdmin):
    order_by = ['-special_point', '-level']
    list_display = ['user', 'special_point', 'level']
    list_filter = ('level', 'special_point')
    search_fields = ('user__username', 'level','special_point')
    
admin.site.register(Activity, AdminActivity)