from django import forms
from Elecbill.models import elecbill

class Elecform(forms.ModelForm):
    class Meta:
        model=elecbill
        fields="__all__"
