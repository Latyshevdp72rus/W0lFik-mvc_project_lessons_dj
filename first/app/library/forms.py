from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from app.library.models import Read_books
from app.library.validators import validation_reads


class ReadsForm(forms.Form):
    last_name = forms.CharField(
        required=True,
        min_length=5,
        label="Фамилия читателя",
        validators=[validation_reads],
        widget=forms.TextInput(attrs={"class": "librarys_text"})
    )

    first_name = forms.CharField(
        required=True,
        min_length=5,
        label="Имя читателя",
        validators=[validation_reads],
        widget=forms.TextInput(attrs={"class": "librarys_text"})
    )

    father_name = forms.CharField(
        required=True,
        min_length=5,
        label="Отчество читателя",
        validators=[validation_reads],
        widget=forms.TextInput(attrs={"class": "librarys_text"})
    )

    reads_query = Read_books.objects.all()
    reads_array =[
        (reads.id, f'{reads.ln_read} {reads.fn_read} {reads.fatn_read}') for reads in reads_query
    ]

    reads = forms.MultipleChoiceField(
        widget=forms.MultipleChoiceField(),
        choices=reads_array,
        label='Читатели',
        required=True
    )

    class Meta:
        model = Read_books
        fields = ['ln_read', 'fn_read', 'fatn_read', 'birthday_read','address_read', 'contact_phone_read', 'read_img']
        widgets = {
            'ln_read': forms.TextInput(attrs={"class": "librarys_text"}),
            'fn_read': forms.TextInput(attrs={"class": "librarys_text"}),
        }
