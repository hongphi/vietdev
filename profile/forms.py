from django import forms
from profile.models import Profile


class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        exclude = [
            "user",
            "joined_date"]