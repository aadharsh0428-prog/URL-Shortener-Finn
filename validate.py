import validators #Framework to check for whether URL is valid or not.
from marshmallow import ValidationError #Framework to echo Validation Error.
from functools import cache #Framework to use caching in Python.
@cache #Decorator function to cache below method.
def check(url): #Functionn to check if URL is valid or not.
    if not url:
        raise ValidationError("Such input data is not accepted") #If URL entered is empty or unsatisfactory datatype.
    else:
        if not validators.url(url): #Condition to check if URL is valid or not
            raise ValidationError("Enter a valid URL")
        else:
            return True


