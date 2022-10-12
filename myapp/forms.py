
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from ckeditor.fields import RichTextField

from myapp.models import Recipe

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style':'border-style: outset;'}))
    first_name= forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','style':'border-style: outset;'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','style':'border-style: outset;'}))

    class Meta:

        model=User
        fields=['username','first_name','last_name','email','password1','password2']

