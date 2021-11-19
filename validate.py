import validators
from marshmallow import ValidationError
from functools import cache
@cache
def check(url):
    if not url:
        raise ValidationError("Such input data is not accepted")
    else:
        if not validators.url(url):
            raise ValidationError("Enter a valid URL")
        else:
            return True


