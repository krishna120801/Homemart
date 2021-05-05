from django import forms
from django.forms import ModelForm
from .models import for_registration,cart

class cartelements(forms.ModelForm):
    class Meta:
        model= cart
        fields=["Cartid","phone_no"]
class PostForm(forms.ModelForm):
    class Meta:
        model = for_registration
        fields = ["name","password","phone_nu","loc"]