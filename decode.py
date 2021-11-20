from unshortenit import UnshortenIt #Framework to unshorten URLs
from functools import cache #Framework to use caching in Python.
@cache #Decorator function to cache below method.
def url_long(url): #Function to unshorten URLs. Shortened URLs is passed as input.
    unshortener = UnshortenIt() #Object is created to access UnshortenIt's function.
    original_url = unshortener.unshorten(url)
    return original_url

