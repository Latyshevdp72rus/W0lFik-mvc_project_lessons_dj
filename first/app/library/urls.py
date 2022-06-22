from django.urls import path
from app.library.views import get_library_list

urlpatterns = [
    path('', get_library_list),
]
