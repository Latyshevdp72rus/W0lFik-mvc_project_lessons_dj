import re
from django.core.exceptions import ValidationError


def validation_reads(ln_read):
    if re.fullmatch(r'[A-ZА-ЯЁ0-9!?:-].*', ln_read):
        return ln_read
    else:
        ValidationError(
            message="не соответствует требованиям: (A-ZА-ЯЁ0-9!?:-)"
        )
