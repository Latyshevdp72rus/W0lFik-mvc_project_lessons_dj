from django.shortcuts import render
from django.http import HttpResponse


def get_library_list(request):
    return HttpResponse("ЗДесь будет Библиотека")
