from django import forms
from .models import Buy


class ChoiseForm(forms.ModelForm):
    class Meta:
        model = Buy
        exclude = ['product']
        fields = '__all__'