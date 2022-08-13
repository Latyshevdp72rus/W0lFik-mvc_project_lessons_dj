import django_filters
from django import forms
from app.library.models import  Read_books


class LibrarysFilter(django_filters.FilterSet):
    read_books_name = django_filters.CharFilter(widget=forms.TextInput(attrs={"class": "filter"}))

    class Meta:
        model = Read_books
        fields = ['read_books_name']
        exclude = ['book_img']
