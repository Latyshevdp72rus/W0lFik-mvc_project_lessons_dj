import re
from django.core.exceptions import ValidationError


def validation_book_name(book_name):
    if re.fullmatch(r'[A-ZА-ЯЁ0-9!?:-].*', book_name):
        return book_name
    else:
        ValidationError(
            message="не соответствует требованиям: (A-ZА-ЯЁ0-9!?:-)"
        )
