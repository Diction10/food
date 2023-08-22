from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import Food

# user registration form

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

        help_texts = {
            'username': None,
            'password1': None,
        }


# User Login Form
class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

        help_texts = {
        'username': None,
    }

# add food form
class AddFoodForm(forms.ModelForm):
    
    class Meta:
        model = Food
        fields = '__all__'
        exclude = ['date_created', 'user']
        