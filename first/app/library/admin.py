from .models import Extradition, Read_books
from django.contrib import admin


class ExtraditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_library_card', 'date_extradition', 'date_delivery',"is_access")
    list_display_links = ('id', 'id_library_card', 'date_extradition', 'date_delivery')
    list_filter = ('id_library_card',)


class ReadBooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'ln_read', 'fn_read', 'fatn_read', 'birthday_read', 'contact_phone_read')
    list_display_links = ('id', 'ln_read', 'fn_read', 'fatn_read', 'birthday_read', 'contact_phone_read')
    search_fields = ('address_read', 'contact_phone_read')
    list_filter = ('ln_read',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('ln_read', 'fn_read', 'fatn_read', 'birthday_read','read_img',)
        }),
        ('Контактная информация', {
            'fields': ('address_read', 'contact_phone_read')
        })
    )


admin.site.register(Extradition, ExtraditionAdmin)
admin.site.register(Read_books, ReadBooksAdmin)
