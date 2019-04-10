from django import forms
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'password']

class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email')
        
class UserCustomChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)