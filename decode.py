from unshortenit import UnshortenIt 
from functools import cache 
@cache
def url_long(url):
    unshortener = UnshortenIt()
    original_url = unshortener.unshorten(url)
    return original_url

