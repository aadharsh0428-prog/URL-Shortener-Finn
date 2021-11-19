import pyshorteners
from functools import cache
@cache
def url_short(url):
    x = pyshorteners.Shortener()
    k=x.tinyurl.short(url)
    return k