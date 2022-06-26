from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def get_books_list(request):
    m_book = Book.objects.get()
    # m_book = Book.objects.all().first()

    return HttpResponse(f"<h1>ww</h1>")
