from django import forms
from . models import Nationality


class NationalityForm(forms.ModelForm):
    class Meta:
        model = Nationality
        fields = '__all__'