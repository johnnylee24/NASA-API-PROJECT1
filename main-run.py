#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import webbrowser
import requests
import ssl
import json
import urllib.request
from flask import Flask, render_template, request, Response
from flask_restplus import Api, Resource, fields, reqparse
from config import Config
from API import response_request_nasa_api
from modules import request_nasa_api
# BASIC APP CONFIG
##################

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['DEBUG'] = True
api = Api(app
        , version=Config.API_VERSION
        , title=Config.API_TITLE
        , description=Config.API_DESCRIPTION
        , default=Config.API_DEFAULT
        , default_label=Config.API_DEFAULT_LABEL)
        
@app.route(Config.INDEX_URL, methods=['GET'])
def app_body():
    return render_template('index.html')

# ENTRY POINT
@app.route('/apiModuleNasa')
def apiModuleNasa():
    this_context = ssl.SSLContext()
    BASE_URL = "https://api.nasa.gov/planetary/apod?api_key="
    request_url = BASE_URL + API_TOKEN
    API_TOKEN = request.args.get('API_TOKEN')
    response = response_request_nasa_api(API_TOKEN)
    Links = urllib.request.urlopen(request_url, context = this_context)
    reader = Links.read()
    responimg = json.loads(reader.decode('utf-8')) responimg = json.loads(reader.decode('utf-8'))  
    return render_template('index.html', responimg['hdurl'])
#
# API → ENTRY POINT
###################
@api.route('/apiModuleNasa?API_TOKEN=<string:API_TOKEN>')
class apiModule(Resource):
    def get(self, API_TOKEN):
        response = response_request_nasa_api(API_TOKEN)
        return response

# APP RUN SETTINGS
##################
# if __name__ == '__main__':
#     app.run(debug=True, host = '0.0.0.0',port=5005, threaded=True)
if __name__ == '__main__':
        app.run(debug=True, host=Config.BIND_IP, port=Config.BIND_PORT, threaded=True)
        
    
