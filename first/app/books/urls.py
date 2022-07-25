from django.urls import path
from app.books.views import BooksDetail,BookList,get_books_list,add_books
urlpatterns = [
    path('', get_books_list),
    path('', BookList.as_view(),name='main'),
    path('add_book/', BookList.as_view(),name='add_book'),
    path('<int:pk>', BooksDetail.as_view(),name='detail_view'),

    # path('<int:id_book>', get_book),

]
