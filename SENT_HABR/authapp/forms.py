from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from authapp.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2', 'email', 'avatar')

    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)
    #     for field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password')

    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)
    #     for field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'
