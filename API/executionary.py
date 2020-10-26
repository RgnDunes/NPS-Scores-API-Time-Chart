import pymongo 
from bson.json_util import dumps

class Executionary:
    def __init__(self):
        db_name="NPS_Data"
        self.client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.ji0rh.mongodb.net/<dbname>?retryWrites=true&w=majority")    # <--------- PASTE HERE
        self.database=self.client[db_name]

    @staticmethod
    def mongoToJson(data):
        json_Data=list(data)
        return json_Data

    def getAllData(self):
        alpha=self.database["NPS_Responses"].find({},{"_id":0})
        beeta=Executionary.mongoToJson(alpha)
        return beeta

    