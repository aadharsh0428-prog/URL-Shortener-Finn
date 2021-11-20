from flask import Flask, request, jsonify # Imports the flask library modules
from flask.wrappers import Response
from marshmallow import ValidationError
import requests as req
import encode
import decode
import json
import validate
import errors_find
app = Flask(__name__) # Single module that grabs all modules executing from this file

@app.route('/encode', methods=['GET']) # HTTP request methods namely "GET" or "POST"
def encode_data():
    url=request.args.get('original_url')
    try:
        value=validate.check(url)
    except ValidationError as error_message:
        return jsonify(error_message.messages),400
    try:
        resp = req.get(url)
    except:
        return jsonify("Could not resolve host"),400
    try:
        code = resp.status_code
        if((code>=200 and code<209) or (code==226)):
           print("Website is alive")
        else:
            return jsonify("Website is inactive"),400
    except:
        return jsonify("Error while checking if website's status"),400
    try:
        short_url=encode.url_short(url)
    except(Exception,):
        return Response(status=errors_find['ServerError'].get('status'), response=errors_find['ServerError'].get('response'))
    return jsonify(short_url)

@app.route('/decode', methods=['GET'])
def decode_data():
    url_new=request.args.get('short_url')
    try:
        value=validate.check(url_new)
    except ValidationError as error_message:
        return jsonify(error_message.messages),400
    try:
        resp = req.get(url_new)
    except:
        return jsonify("Could not resolve host"),400
    try:
        code = resp.status_code
        if((code>=200 and code<209) or (code==226)):
           print("Website is alive")
        else:
            return jsonify("Website is dead"),400
    except:
        return jsonify("Error while checking if website's status"),400
    try:
        long_url=decode.url_long(url_new)
    except(Exception,):
        return Response(status=errors_find['ServerError'].get('status'), response=errors_find['ServerError'].get('response'))
    return jsonify(long_url)

    
