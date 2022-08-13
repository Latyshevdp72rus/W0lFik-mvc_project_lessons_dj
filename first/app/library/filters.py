import django_filters
from django import forms
from app.library.models import Read_books,Extradition


class ReadBooksFilter(django_filters.FilterSet):
    read_books_query = Read_books.objects.all()
    last_name = django_filters.CharFilter()
    read_books_name = django_filters.ModelChoiceFilter(queryset=Read_books.objects.all())

    class Meta:
        model = Read_books
        fields = ['last_name']
        exclude = ['book_img']
