from django import forms
from .models import Fchat

class FchatForm(forms.ModelForm):
    class Meta:
        model = Fchat
        fields = ['message', 'sender']  # Assuming you have a 'message' and 'sender' field in your model
