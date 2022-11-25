from django import forms
from .models import Player
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('playerName', 'runs', 'team', 'records')



