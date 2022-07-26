import re

from django.core.exceptions import ValidationError


def validation_book_name(book_name):
    if re.fullmatch(book_name,r'Книга.*'):
        return book_name
    else: ValidationError(message="Не соответствует требованию")
