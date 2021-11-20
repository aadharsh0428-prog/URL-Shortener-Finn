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

```In this REST-API there are 2 end-points/functionality namely encode and decode.<br>
   1./encode: Shortens the original URL into a short URL and checks for corresponding boundary conditions.
   2./decode: Converts a shortened URL back to the original URL and checks for corresponding boundary conditions.
```

# File Description

```
1.decode.py: File which contains function to deshorten shortened URL back to the original URL.
2.encode.py: File which contains function to shorten original URL into Tiny URL.
3.errors_find.py: File which contains a dictionary to classify into whether they are server error or bad request 
                  and return a corresponding status code.
4.requirements.txt: Has the list of python libraries that needs to be installed to run this microservice.
5.run.py: The pipeline of this microservice is present in this file. The corresponding end points 
          are written here using decorator functions. 
6.validate.py: File which checks if the given URL sent is valid or not. 

For faster access and execution all the functions written in the above files have been cached and built in python functions have been used for shortening<br> and
deshortening the URLs.

```
# Steps for execution

### Disclaimer

```
Do install Postman for easier passage of requests and to see outputs as well.
```
Click [here](https://www.postman.com/downloads/) to go to the downloads page.

### Clone repository
After cloning the repository using the git clone command on the terminal perform the below operations.

```
$> cd the-shortest-url-1-uvpyns
$> pip install -r requirements.txt / pip3 install -r requirements.txt 
```
Based on Python version use pip or pip3.

### Setting up flask environment
After installing the required libraries to execute this code we shall now set up the flask environment to run the 2 endpoints.<br>
Note this is running it on the localhost.<br>

```
$> export FLASk_APP=run.py
$> export FLASK_ENV=development
$> flask run
```
### Result visualisation on Postman
Post setting up the flask environment the API is hosted on the local host and is running.<br> To pass requests and check outputs we use Postman. <br>

```
1.Install Postman and create a free account using Gmail.
2.Create a new request by clicking on the + symbol.
3.Enter the URL http://127.0.0.1:5000/encode or http://127.0.0.1:5000/decode for appropriate usage.
4.For passing requests make sure that the method of transaction is GET. 
5.For encode the key is original_url and value is a URL of your choice.
6.For decode the key is short_url and value is a shortened URL of your choice.
7.Output can be seen on the window named "Pretty" under the Body section.
8.Check for status codes and messages/exceptions(if any) in the terminal after you pass the request on Postman.
```
