from django.urls import path
from app.library.views import get_reads_book, ReadList, ReadDetail, ReadCreateView

urlpatterns = [
    # path('', get_reads_book),
    path('', ReadList.as_view(), name='main'),
    path('<int:pk>/', ReadDetail.as_view(), name='detail_view'),
    path('add_new', ReadCreateView.as_view(), name='add_new'),

]
