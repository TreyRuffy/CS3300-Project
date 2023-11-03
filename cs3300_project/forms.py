from django.forms import ModelForm

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