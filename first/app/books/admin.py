from app.books.models import Book, PublishingHouse, Author, BookInlineAuthor
from django.contrib import admin


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'description', 'id_publishing_house', 'date_creation', 'date_add', 'is_daleted')
    list_display_links = ('id', 'book_name')
    search_fields = ('book_name',)
    list_editable = ('is_daleted',)
    list_filter = ('date_creation', 'book_name', 'is_daleted')
    fieldsets = (
        (None, {
            'fields': ('book_name', 'description', 'id_publishing_house', 'book_img')
        }),
        ('Дата', {
            'fields': ('date_creation',)
        })
    )


class PublishingHouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'pub_house_name', 'pub_house_address', 'pub_house_contact_phone', 'pub_house_email',
                    'pub_house_site', 'date_add', 'is_daleted')
    list_display_links = ('id', 'pub_house_name',)
    search_fields = ('pub_house_name',)
    list_editable = ('is_daleted',)
    list_filter = ('date_add', 'is_daleted')
    fieldsets = (
        (None, {
            'fields': ('pub_house_name', 'pub_house_address')
        }),
        ('Контактная информация', {
            'fields': ('pub_house_contact_phone', 'pub_house_email', 'pub_house_site')
        })
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'father_name', 'country', 'birthday', 'languages',
                    'date_add', 'is_daleted')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'last_name', 'father_name')
    list_editable = ('is_daleted',)
    list_filter = ('last_name', 'country', 'is_daleted')

    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'father_name', 'country', 'birthday', 'languages', 'is_daleted')
        }),
    )

    inlines = [
        BookInlineAuthor,
    ]


admin.site.register(Book, BookAdmin)
admin.site.register(PublishingHouse, PublishingHouseAdmin)
admin.site.register(Author, AuthorAdmin)
