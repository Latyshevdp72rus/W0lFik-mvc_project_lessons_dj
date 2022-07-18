from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets


class LoginForm(forms.Form):
    user_name = forms.CharField(
        max_length=20,
        label="Логин:"
    )

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['user_name', 'password']


class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        max_length=20,
        label="Имя:"
    )
    last_name = forms.CharField(
        max_length=20,
        label="Фамилия:"
    )
    email = forms.EmailField(
        label="Email: ",
        max_length=20)

    user_name = forms.CharField(
        max_length=20,
        label="Логин:"
    )

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']
