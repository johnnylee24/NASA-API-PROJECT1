#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os
import requests
import urllib.request
import ssl
import json
import webbrowser
from flask import Flask, render_template, request, Response

def request_nasa_api(API_TOKEN):
    this_context = ssl.SSLContext()
    BASE_URL = "https://api.nasa.gov/planetary/apod?api_key="
    request_url = BASE_URL + API_TOKEN
    response = requests.get(request_url)
    Links = urllib.request.urlopen(request_url, context = this_context)
    reader = Links.read()
    responimg = json.loads(reader.decode('utf-8'))
    webbrowser.register('chrome', None, webbrowser.GenericBrowser('chrome'), 1)
    return webbrowser.get('chrome').open('index.heml',Pic = responimg['url'])
    
#     return render_template('index.html', Pic = responimg['url'])

    

    

    



     
    

   

