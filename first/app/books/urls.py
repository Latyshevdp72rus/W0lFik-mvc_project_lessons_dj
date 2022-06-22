from django.urls import path
from app.books.views import get_books_list

urlpatterns = [
    path('', get_books_list),
]
