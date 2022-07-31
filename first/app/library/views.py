from django.shortcuts import render
from django.http import HttpResponse
from app.library.models import Read_books, Extradition
from django.views.generic import ListView, DetailView, CreateView, FormView


# Создайте новый шаблон, на который виведите данные из созданного вами ранее приложения книжного магазина/библиотеки
# Результат домашнего задания: ссылка на репазиторий github
def get_reads_book(request):
    reads = Extradition.objects.all()
    context = {
        'reads': reads,
    }
    return render(request, 'librarys/all_library.html', context)


class ReadList(ListView):
    model = Extradition
    context_object_name = 'reads'
    template_name = 'librarys/library_list.html'

    def get_queryset(self):
        return Extradition.objects.filter(is_access=True)


class ReadDetail(DetailView):
    model = Extradition
    pk_url_kwarg = 'pk'
    context_object_name = 'reads'
    template_name = 'librarys/library_detail.html'
