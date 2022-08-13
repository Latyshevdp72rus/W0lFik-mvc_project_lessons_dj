from django_filters.views import FilterView
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse_lazy
from app.books.models import Book, Author
from app.books.forms import BookForm
from app.books.filters import BookFilter
from app.books.validators import validation_book_name


# from app.books.validators import validation_book_name
# class BookList(ListView):
class BookList(FilterView):
    model = Book
    filterset_class = BookFilter
    context_object_name = 'books'
    template_name = 'books/book_list.html'
    paginate_by = settings.OBJECTS_ON_PAGE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.queryset
        context['title'] = 'Городская библиотека'
        return context


class BooksDetail(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    pk_url_kwarg = 'pk'


class CreateBookView(CreateView):
    model = Book
    model_form = BookForm
    template_name = 'books/add_book.html'
    success_url = reverse_lazy('add_book')
    fields = ['book_name', 'description', 'author','book_img']
