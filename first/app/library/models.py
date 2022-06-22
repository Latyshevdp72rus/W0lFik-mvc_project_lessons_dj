from django.db import models


class Library(models.Model):
    library_name = models.CharField(max_length=100, verbose_name="Название Библиотеки")
