from django.urls import path
from app.books.views import BooksDetail, BookList, add_books,get_books_list

urlpatterns = [
    path('',get_books_list),
    path('', BookList.as_view(), name='main'),
    path('<int:pk>', BooksDetail.as_view(), name='detail_view'),
    path('add_book/', add_books, name='add_book'),

    # path('<int:id_book>', get_book),

]
