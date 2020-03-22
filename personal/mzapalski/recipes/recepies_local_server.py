import json
import logging
import os

from flask import Flask, flash, redirect, request, send_from_directory, session, url_for
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename

import requests
from bs4 import BeautifulSoup

def get_url(url):
    try:
        r = requests.get(url)
    except Exception as e:
        print(e)
        return None
    else:
        return r.text

def GetIngrsFromKuchniaLidla(url):
    bs = BeautifulSoup(get_url(url), 'lxml')
    a = bs.findAll("div", {"class": "skladniki"})
    ings = a[0].find_all('li')
        
    clean_ings = []
    
    for item in ings:
        a = item.text.split(' – ')
        if(len(a)<2):
            quantity=''
        else:
            quantity = a[1]
        name = a[0]
        clean_ings.append((name, quantity))
        
    a = bs.findAll("li", {"class": "meta_size"})
    if(len(a)>0 ):
        n_portions = int(a[0].contents[0])
    else:
        n_portions = None
    
    return {'url':url,
           'ingredients':clean_ings,
           'portions':n_portions}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("recipy")

app = Flask(__name__)
CORS(app, expose_headers="Authorization")


@app.route("/", methods=["POST","GET"])
def generate_list():
    logger.info("Generating list.")
    print(request.data)
    lista_url = json.loads(request.data)
    print(lista_url)
    response = {
        'data': 'got it!',
    }
    response = []
    for item in lista_url:
    	response.append(GetIngrsFromKuchniaLidla(item['url']))

    a = {'output':response}
    return a

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="0.0.0.0", use_reloader=False)