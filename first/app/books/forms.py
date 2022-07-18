from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.models import User
from app.books.models import Book, Author


class BookForm(forms.Form):
    author_query = Author.objects.all()
    author_arr = (
        ([author.first_name, author.last_name]) for author in author_query
    )

    book_name = forms.CharField(min_length=4, label='Название книги')
    author = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        choices=author_arr,
        label='Авторы',
        required=True,
    )
    # author_name = forms.CharField()
    # description = forms.CharField(min_length=5, label='Описание книги')


class LoginForm():
    ...


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
