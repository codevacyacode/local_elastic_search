# -*- coding: utf-8 -*-

"""
Created on Sat May 22 17:21:53 2021

@author: codevacyacode

$ python app.py

"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from elasticsearch import Elasticsearch
import json

def connect_elasticsearch():
    """
    Подключение к elasticsearch
    """
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Есть контакт!')
    else:
        print('Вас не слы...бжжж')
    return _es
    
def search(es_object, index_name, search):
    """
    Поиск
    """
    res = es_object.search(index=index_name, body=search)
    return res

# конфигурация
DEBUG = False

# создание и инициализация приложения
app = Flask(__name__)
app.config.from_object(__name__)

# включить CORS
CORS(app)
    
# поиск и вывод
@app.route('/search', methods=['GET', 'POST'])
def search_that():
    post_data = request.get_json()
    that = post_data.get('query0')
    fuz = post_data.get('fuzziness')
    if fuz != "AUTO":
        fuz = int(fuz)
    es = connect_elasticsearch()
    if es is not None:
        search_object = {
            "min_score": 12.0,
            "query": 
            {
                "match": {
                    "text": {
                        "query": that,
                        "fuzziness": fuz,
                    }
                }
            },
            "size": 50,
            "sort": [
                {
                    "_score": "desc",
                    "date": "desc"
                }
            ]
        }
        found = es.search(index = 'news', body = json.dumps(search_object))
        output = {}
        i = 0
        for hit in found['hits']['hits']:
            i += 1
            output.update(
                {
                    i: {
                        "Номер": i,
                        "Название": hit["_source"]["title"], 
                        "Дата": hit["_source"]["date"], 
                        "Текст": hit["_source"]["text"]
                    }
                }
            )
        return output

if __name__ == "__main__":
    app.run()