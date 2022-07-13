from django import forms
from django.contrib.admin import widgets
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


