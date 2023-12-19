from django import forms
from .models import MusiciansModel

class addmusicianform(forms.ModelForm):
    class Meta :
        model = MusiciansModel
        fields = '__all__'