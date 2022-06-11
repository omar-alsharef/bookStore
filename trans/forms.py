from django import forms
from .models import Trans

class TransForm(forms.ModelForm):
    class Meta:
        model = Trans 
        fields = '__all__' 