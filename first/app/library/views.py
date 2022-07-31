from django.shortcuts import render
from django.http import HttpResponse
from app.library.models import Read_books,Extradition


# def get_library_list(request):
#     return HttpResponse("ЗДесь будет Библиотека")

# Создайте новый шаблон, на который виведите данные из созданного вами ранее приложения книжного магазина/библиотеки
# Результат домашнего задания: ссылка на репазиторий github
def get_reads_book(request):
    reads= Extradition.objects.all()
    # reads = Read_books.objects.all()
    context = {
        'reads': reads,
    }
    return render(request,'librarys/all_library.html',context)
