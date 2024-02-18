from pymongo import MongoClient

class MongodbQuery:
    def __init__(self,db_name='mydb',collection_name='mycolletion',username = None, password = None):
        """
        :param host:str mongodb host address
        :param db_name: str name of database
        :collection_name: str name of collection
        :param port: int port
        """
        client = MongoClient(username=username, password=password)
        self.db = client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, dic):
        return self.collection.insert_one(dic)
    
    def insert_many(self, lists):
        return self.collection.insert_many(lists)
    
    def find_one(self, dic):
        return self.collection.find_one(dic)
    
    def find(self, dic):
        return list(self.collection.find(dic))

    def update_one(self, dic):
        return self.collection.update_one(dic,{'$set':dic}, upsert=True)
    
    def update_many(self, dic):
        return self.collection.update_many(dic,{'$set':dic}, upsert=True)
    
    def delete_one(self, dic):
        return self.collection.delete_one(dic)
    
    def delete_many(self, dic):
        return self.collection.delete_many(dic)