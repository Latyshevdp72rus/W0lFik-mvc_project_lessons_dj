import django_filters
from app.books.models import Book, Author


class BookFilter(django_filters.FilterSet):
    author_query = Author.objects.all()
    book_name = django_filters.CharFilter()
    author = django_filters.ModelChoiceFilter(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['book_name', 'author']
        exclude = ['book_img']

