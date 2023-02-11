from pymongo import MongoClient

def connectToDB():
    client = MongoClient("mongodb://deepak_belamana:deepak1304@cluster0-shard-00-00.cgjfy.mongodb.net:27017,cluster0-shard-00-01.cgjfy.mongodb.net:27017,cluster0-shard-00-02.cgjfy.mongodb.net:27017/?ssl=true&replicaSet=atlas-38mjyj-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client.BlogCMS
    return db