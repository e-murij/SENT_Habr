from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from authapp.models import User, UserProfile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}), label='Никнейм')
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}), label='Имя')
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name'}), label='Фамилия')
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1'}), label='Пароль')
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password2'}), label='Повторить пароль')
    email = forms.EmailField(max_length=200,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}),
                             label='Электронная почта')
    avatar = forms.FileField(required=False,
                             widget=forms.FileInput(attrs={'class': 'form-control', 'name': 'avatar',
                                                           'style': "border-color: #1bafd5"}), label='Аватар')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'avatar')


class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Никнейм'}),
        label='Никнейм')
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Пароль'}),
        label='Пароль')

    class Meta:
        model = User
        fields = ('username', 'password')


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}), label='Никнейм')
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name'}), label='Имя')
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name'}), label='Фамилия')
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}), label='Электронная почта')
    avatar = forms.FileField(required=False,
                             widget=forms.FileInput(attrs={'class': 'form-control', 'name': 'avatar',
                                                           'style': "border-color: #1bafd5"}), label='Аватар')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'avatar']


class UpdateProfileForm(forms.ModelForm):
    about_me = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
                               label='Обо мне')
    gender = forms.ChoiceField(required=False, widget=forms.RadioSelect,
                               choices=UserProfile.GENDER_CHOICES)
    birthday = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
                               label='Дата рождения')

    class Meta:
        model = UserProfile
        fields = ['gender', 'birthday', 'about_me']
