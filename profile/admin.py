from django.contrib import admin
from profile.models import Profile


class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'gender', 'birthday', 'joined_date']
    list_filter = ('joined_date',)
    search_fields = ('user',)
    
    
admin.site.register(Profile, AdminProfile)