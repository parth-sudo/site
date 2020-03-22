from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Paytm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']



class PaytmForm(forms.ModelForm):
    choices = forms.ChoiceField(choices=[('Squad-₹40', 'Squad-₹40'),
                                         ('Duo-₹30', 'Duo-₹30'),
                                         ('Solo- ₹20','Solo-₹20')])

    class Meta:
        model = Paytm
        fields = ['username', 'email', 'phone_number', 'choices', 'amount']

