from django_filters.views import FilterView
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse_lazy
from app.library.models import Extradition,Read_books
from app.library.forms import ReadsForm
from app.library.filters import ReadBooksFilter
from app.library.validators import validation_reads


class ReadList(ListView):
    model = Extradition
    context_object_name = 'reads'
    template_name = 'librarys/library_list.html'
    paginate_by = settings.OBJECTS_ON_PAGE

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['reads'] = self.queryset
#         context['title'] = 'Городская библиотека'
#         return context
# #
    def get_queryset(self):
        return Extradition.objects.filter(is_access=True)

class ReadDetail(DetailView):
    model = Extradition
    pk_url_kwarg = 'pk'
    context_object_name = 'reads'
    template_name = 'librarys/library_detail.html'


class ReadCreateView(CreateView):
    model = Read_books
    model_form = ReadsForm
    template_name = 'librarys/add_reads.html'
    success_url = reverse_lazy('add_reads')
    fields = ['ln_read', 'fn_read','read_img']





