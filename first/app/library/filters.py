import django_filters
from django import forms
from app.library.models import Extradition


class LibrarysFilter(django_filters.FilterSet):
    librarys_name = django_filters.CharFilter(widget=forms.TextInput(attrs={"class": "filter"}))

    class Meta:
        model = Extradition
        fields = ['librarys_name']
        exclude = ['book_img']
