from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create forms here
from .models import Horse, BuyableHorse

class HorseForm(ModelForm):
    class Meta:
        model = Horse
        fields = ['name', 'short_description', 'long_description', 'image']

class BuyableHorseForm(ModelForm):
    class Meta:
        model = BuyableHorse
        fields = ['horse', 'price']

class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']