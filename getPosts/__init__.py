import logging
import azure.functions as func
import pymongo
import json
import sys
import ssl
import certifi
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://cosmosaccountdhruv:fsivyka2LVu3xZfCUeMnk5kAaECSgIN7DZNp8XRlbZQnpHvDqThzkTz1s03dceV6EpL84U9IdsFYACDbIUlxGQ==@cosmosaccountdhruv.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@cosmosaccountdhruv@"

        logging.info(
            f"Env diagnostic: python={sys.version} openssl={ssl.OPENSSL_VERSION} pymongo={pymongo.version}"
        )

        client = pymongo.MongoClient(
            url,
            serverSelectionTimeoutMS=8000,
            tlsCAFile=certifi.where(),
            tlsAllowInvalidCertificates=True,
        )

        database = client['azure']
        collection = database['posts']
        result = list(collection.find({}))
        return func.HttpResponse(dumps(result), mimetype="application/json", charset='utf-8', status_code=200)
    except Exception as e:
        logging.error(f"Error in getPosts: {e}", exc_info=True)
        return func.HttpResponse(f"Error: {e}", status_code=500)
