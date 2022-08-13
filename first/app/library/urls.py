from django.urls import path
from app.library.views import ReadList, ReadDetail, ReadCreateView

urlpatterns = [
    path('', ReadList.as_view(), name='library'),
    path('<int:pk>/', ReadDetail.as_view(), name='detail_view'),
    path('add_library/', ReadCreateView.as_view(), name='add_reads'),

]
