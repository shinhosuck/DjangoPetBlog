from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from users.models import Profile, Contact
from django import forms

class UserRegisterForm(UserCreationForm ):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields =  ["username", "email"]

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile 
        fields = ["image"]


class ContactUsForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Contact
        fields = ["email", "content"]