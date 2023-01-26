from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserProfileUpdate(forms.Form):
    first_name = forms.CharField(max_length=60)
    last_name = forms.CharField(max_length=60)
    email = forms.EmailField()
    password = forms.CharField(max_length=20,min_length=8)
    confirm_password = forms.CharField(max_length=20,min_length=8)


    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data['password']
        if password != confirm_password:
            self.add_error('confirm_password','password doesn\'t match!')
