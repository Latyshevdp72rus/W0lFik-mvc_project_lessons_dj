from django.urls import path
from app.books.views import BooksDetail,BookList,get_books_list
urlpatterns = [
    path('', get_books_list),
    path('', BookList.as_view()),
    path('<int:pk>', BooksDetail.as_view()),

    # path('<int:id_book>', get_book),

]
