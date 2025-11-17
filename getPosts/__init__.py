import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://cosmosaccountdhruv:fsivyka2LVu3xZfCUeMnk5kAaECSgIN7DZNp8XRlbZQnpHvDqThzkTz1s03dceV6EpL84U9IdsFYACDbIUlxGQ==@cosmosaccountdhruv.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosaccountdhruv@"
        client = pymongo.MongoClient(url)
        database = client['db']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)
    except Exception as e:
        logging.error('Operational failure in getPosts: %s\n%s', e, traceback.format_exc())
        return func.HttpResponse(f"Operational error: {e}", status_code=500)
