from django.urls import path
from app.books.views import BooksDetail, BookList, CreateBookView


urlpatterns = [
    path('', BookList.as_view(), name='main'),
    path('<int:pk>', BooksDetail.as_view(), name='detail_view'),
    path(r'add_book/', CreateBookView.as_view(), name='add_book'),

]
