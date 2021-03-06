from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        exclude = ('created_on' , 'updated_on', 'user',)