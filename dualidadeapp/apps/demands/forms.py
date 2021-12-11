from django import forms
from .models import Demand, DemandTeamLike

class DemandForm(forms.ModelForm):

    class Meta:
        model = Demand
        exclude = ('created_on' , 'updated_on')


class DemandTeamLikeForm(forms.ModelForm):
    
    class Meta:
        model = DemandTeamLike
        exclude = ('created_on' , 'updated_on', 'demand')