from django.http import HttpResponse
from .models import Author, PublishingHouse, Book


def get_books_list(request):
    # m_book = Book.objects.get()
    # m_book = Book.objects.get(id_publishing_house__pub_house_name="Издательство 3")
    # print(m_book.book_name)
    # # m_book = Book.objects.all().first()
    # pub_query = PublishingHouse.objects.all()
    # author_query = Author.objects.filter(pk=1).prefetch_related('books')
    # for i in pub_query:
    #     pubg = i
    #
    # for j in author_query:
    #     author = i
    # books = author.book.first()
    # print(books)

    # author_query = Author.objects.filter(pk=1).prefetch_related('books')
    # for a in author_query:
    #     author = a
    # context = {
    #     "author": author,
    # }

    # pub_query = PublishingHouse.objects.prefetch_related('publishinghouse_books').all()

    # for pub_house in pub_query:
    #     for book in pub_house.publishinghouse_books.all():
    #         print(book.book_name)
    #

    # pub_query = PublishingHouse.objects.values(
    #     'pub_house_name',
    #     'pub_house_site'
    # )

    # pub_query = PublishingHouse.objects.exclude(
    #     is_daleted=False,
    # )
    # for pub_house in pub_query:
    #     publisher = pub_house
    #     print(publisher)
    #
    # return HttpResponse(f"<h1>{publisher}</h1>")

    author_list = (
        Author(first_name="имя1",last_name='фам1' ,country='Россия' ,birthday="2002-01-02"),
        Author(first_name="имя2", last_name='фам2', country='Россия', birthday="2002-01-02"),
        )
    Author.objects.bulk_create(
        author_list
    )
    return HttpResponse(f"<h1>ok</h1>")