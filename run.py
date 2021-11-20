from flask import Flask, request, jsonify # Imports the flask library modules
from flask.wrappers import Response 
from marshmallow import ValidationError #Framework to echo Validation Error.
import requests as req #Framework to pass requests to the server
import encode #Program to shorten the URLs
import decode #Program to unshorten the URLs
import json
import validate #Program to check if the URLs sent are valid or not.
import errors_find #Program to echo errors
app = Flask(__name__) # Single module that grabs all modules executing from this file

@app.route('/encode', methods=['GET']) #Endpoint to shorten URLs.
def encode_data():
    url=request.args.get('original_url') #Statement to extract the URL from the request passed.
    try:
        value=validate.check(url) #Try block for URL validity.
    except ValidationError as error_message:
        return jsonify(error_message.messages),400
    try:
        resp = req.get(url) #Try block to check for if the URL exists or not.
    except:
        return jsonify("Could not resolve host"),400
    try:
        code = resp.status_code #Try block to check if website is up or down based on the status code returned.
        if((code>=200 and code<209) or (code==226)):
           print("Website is alive")
        else:
            return jsonify("Website is inactive"),400
    except:
        return jsonify("Error while checking if website's status"),400
    try:
        short_url=encode.url_short(url) #Try block to receive the shortened URL.
    except(Exception,):
        return Response(status=errors_find['ServerError'].get('status'), response=errors_find['ServerError'].get('response'))
    return jsonify(short_url)

@app.route('/decode', methods=['GET']) #Endpoint to unshorten URLs.
def decode_data():
    url_new=request.args.get('short_url') #Statement to extract the URL from the request passed.
    try:
        value=validate.check(url_new) #Try block for URL validity.
    except ValidationError as error_message:
        return jsonify(error_message.messages),400
    try:
        resp = req.get(url_new) #Try block to check for if the URL exists or not.
    except:
        return jsonify("Could not resolve host"),400
    try:
        code = resp.status_code #Try block to check if website is up or down based on the status code returned.
        if((code>=200 and code<209) or (code==226)):
           print("Website is alive")
        else:
            return jsonify("Website is dead"),400
    except:
        return jsonify("Error while checking if website's status"),400
    try:
        long_url=decode.url_long(url_new) #Try block to receive the unshortened URL.
    except(Exception,):
        return Response(status=errors_find['ServerError'].get('status'), response=errors_find['ServerError'].get('response'))
    return jsonify(long_url)

    
