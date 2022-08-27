from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class UserRegisterFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username'})
        self.fields['email'].widget = forms.EmailInput( attrs={'placeholder': 'Email'})
        self.fields['password1'].widget = forms.PasswordInput( attrs={'placeholder': 'New password' })
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Repeat password'}) 

class UserForm(ModelForm):
    class Meta:
        model = Profile
        fields = [ 'name', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field, in self.fields.items():
            field.widget.attrs.update({'class' : 'input-group'})

