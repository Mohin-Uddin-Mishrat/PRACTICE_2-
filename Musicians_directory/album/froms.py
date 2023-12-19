from django import forms
from .models import albumModel

class addAlbum(forms.ModelForm):
    class Meta :
        model = albumModel
        fields = '__all__'