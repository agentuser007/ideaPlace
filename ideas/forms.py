from django import forms
from .models import Idea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ('title', 'content', 'image')
    image = forms.ImageField(required=False)
