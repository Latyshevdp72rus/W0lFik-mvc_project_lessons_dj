from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from app.books.models import Book, Author
from app.books.validators import validation_book_name


class BookForm(forms.Form):
    book_name = forms.CharField(
        required=True,
        min_length=4,
        label='Название книги',
        validators=[validation_book_name],
        widget=forms.TextInput(attrs={"class": "librarys_text"})
    )
    description = forms.TimeField(
        required=True,
        label='Описание книги',
        widget=forms.Textarea(attrs={"class": "librarys_textarea"})
    )

    author_query = Author.objects.all()
    author_array = [
        (author.id, f'{author.last_name} {author.first_name} {author.father_name}') for author in author_query
    ]
    # [author.id,fauthor.last_name, author.last_name] for author in author_query

    author = forms.MultipleChoiceField(
        widget=forms.MultipleChoiceField(),
        choices=author_array,
        label='Авторы',
        required=True
    )

    class Meta:
        model = Book
        fields = ['book_name', 'description', 'date_creation', 'author', 'id_publishing_house', 'book_img']
        widgets = {
            'book_name': forms.TextInput(attrs={"class": "librarys_text"}),
            'description': forms.Textarea(attrs={"class": "librarys_textarea"}),
            'author': forms.Select(attrs={"class": "librarys_textarea"}),


        }
