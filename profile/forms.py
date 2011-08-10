from django import forms
from profile.models import Profile, UserSettings


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        exclude = ("user", "joined_date")
        

class UserSettingsForm(forms.ModelForm):
    
    class Meta:
        model = UserSettings
        exclude = ('user',)