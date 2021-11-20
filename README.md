# URL-Shortener-Finn

The aim of this project/repository is to create an end to end REST-API to shorten and deshorten URLs.<br> The microservice was written using Flask framework.<br>

# Project Management

```bash
root/
 |-- decode.py
 |-- encode.py  
 |-- errors_find.py
 |-- README.md
 |-- requirements.txt
 |-- run.py
 |-- validate.py
```
# Project Description

In this REST-API there are 2 end-points/functionality namely encode and decode.<br>
1./encode: Shortens the original URL into a short URL and checks for corresponding boundary conditions.<br>
2./decode: Converts a shortened URL back to the original URL and checks for corresponding boundary conditions.

# File Description

1.decode.py: File which contains function to deshorten shortened URL back to the original URL.<br>
2.encode.py: File which contains function to shorten original URL into Tiny URL.<br>
3.errors_find.py: File which contains a dictionary to classify into whether they are server error or bad request and return a corresponding status code.<br>
4.requirements.txt: Has the list of python libraries that needs to be installed to run this microservice.<br>
5.run.py: The pipeline of this microservice is present in this file. The corresponding end points are written here using decorator functions. <br>
6.validate.py: File which checks if the given URL sent is valid or not. <br>

For faster access and execution all the functions written in the above files have been cached and built in python functions have been used for shortening<br> and
deshortening the URLs.<br>
