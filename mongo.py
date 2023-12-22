from pymongo import MongoClient
import json

def add_mongo(dataframe, collection):

    data_json = dataframe.to_json(orient='records')
    data_list = json.loads(data_json)
    collection.insert_many(data_list)
    print(f"Documentos adicionados ao MongoDB. Total: {len(data_list)}")

def salvando(dataframe):
    try:
        client = MongoClient('localhost', 27017)
        db = client["speedio"]
        collection = db["dani"]
        add_mongo(dataframe, collection)
        client.close()
        print("conexçao feita com sucesso")
    except Exception as e:
        print("erro ao salvar")
        raise
