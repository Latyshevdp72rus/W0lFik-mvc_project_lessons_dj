from django.urls import path
from app.library.views import get_reads_book

urlpatterns = [
    path('', get_reads_book),
]
