import pyshorteners #Framework to shorten URLs.
from functools import cache #Framework to use caching in Python.
@cache #Decorator function to cache below method.
def url_short(url): #Function to shorten URLs. Long URLs are passed as inputs.
    x = pyshorteners.Shortener() #Object is created to access pyshorteners' functions.
    k=x.tinyurl.short(url) #Step where shortened URL is returned as a string.
    return k