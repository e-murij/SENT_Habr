from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
    class Meta:
        model = User
        fields = ('username', 'password')

    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)
    #     for field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'
