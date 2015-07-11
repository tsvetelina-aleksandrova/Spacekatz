from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from backend.db.db_obj import DBObject


class DBWorker:

    def __init__(self):
        # connect to default port 28017 on localhost
        self.client = MongoClient()

    def create(self, new_obj):
        self.__check_is_dbobject_instance(new_obj)
        # when a new document is created, an id is generated
        # we return this id and use it to identify DBObjects
        insert_query = self.collection.insert_one(new_obj.get_as_dict())
        return insert_query.inserted_id

    def get_all(self):
        return self.collection.find({})

    def delete(self, obj_to_delete):
        self.__check_is_dbobject_instance(obj_to_delete)
        if not obj_to_delete.is_id_set():
            err_msg = "DBObject needs to have an id in order to be deleted"
            raise AttributeError(err_msg)
        self.collection.remove({'_id': obj_to_delete.get_id()})

    def delete_all(self):
        self.collection.remove({})

    def __check_is_dbobject_instance(self, db_obj):
        if not isinstance(db_obj, DBObject):
            raise TypeError("DBWorker works with DBObjects")


class DBScoreWorker(DBWorker):

    def __init__(self):
        DBWorker.__init__(self)
        self.db = self.client.spacekatz
        self.collection = self.db.scores

    def get_all(self):
        return self.collection.find({}).sort("points", DESCENDING)
