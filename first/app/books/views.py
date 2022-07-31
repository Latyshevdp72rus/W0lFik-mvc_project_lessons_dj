from django_filters.views import FilterView
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.shortcuts import render
from django.core.paginator import Paginator
from app.books.validators import validation_book_name
from app.books.filters import BookFilter
from app.books.models import Book, Author, PublishingHouse
from app.books.forms import BookForm
from django.conf import settings


class BookList(ListView):
    model = Book
    filterset_class = BookFilter
    context_object_name = 'books'
    template_name = 'books/book_list.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.queryset
        context['title'] = 'Городская библиотека'
        return context


def get_books_list(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['book_name']
            book_desc = form.cleaned_data['description']
            authors = form.cleaned_data['author']
    form = BookForm()
    books = Book.objects.all()
    filter = BookFilter(request.GET, queryset=Book.objects.all())
    context = {
        # 'books':books,
        'filter': filter,
        'form': form
    }
    return render(request, 'books/book_list.html', context=context)


def add_books(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book_name = validation_book_name(form.cleaned_data['book_name'])
            authors = form.cleaned_data['author']
    form = BookForm()
    context = {
        'form': form
    }
    return render(request, 'books/add_book.html', context=context)


class BooksDetail(DetailView):
    model = Book
    # template_name = 'books/book_detail.html'
    pk_url_kwarg = 'pk'
