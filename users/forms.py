from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.password_validation import validate_password


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=True, validators=[validate_password])
    password2 = forms.CharField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'phone', 'avatar', 'city', 'address']

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists.')
        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exist.')
        return email


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']




