import django_filters
from django import forms
from app.books.models import Book, Author, PublishingHouse


class BookFilter(django_filters.FilterSet):
    author_query = Author.objects.all()
    book_name = django_filters.CharFilter()
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all())

    class Meta:
        model = Book
        exclude = ['book_img']
        # query = Book.objects.all()
        fields = ['book_name','author']
