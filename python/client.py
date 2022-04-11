from datetime import datetime
import json
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}


with open('../dataExample.json') as file:
    jsonFile = json.load(file)

    for user in jsonFile:
        id = user.pop('id')
        es.create(
            index='users',
            document=user,
            id=id
        )
