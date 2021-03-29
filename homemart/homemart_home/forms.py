from django import forms
from django.forms import ModelForm
from .models import for_registration

class PostForm(forms.ModelForm):
    class Meta:
        model = for_registration
        fields = ["name","password","phone_nu","loc"]