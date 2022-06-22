from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def get_books_list(request):
    m_book = Book.objects.get(pk=7)
    return HttpResponse(f"<h1>{m_book}</h1>")
