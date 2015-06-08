from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING
from sources.db_obj import DBObject

class DBWorker:

	def __init__(self):
		# connect to default port 28017 on localhost 
		self.client = MongoClient()

	def create(self, new_obj):
		if not isinstance(new_obj, DBObject):
			raise TypeError("Expected DBObject")
		score_id = self.collection.insert_one(new_obj.get_as_map()).inserted_id
		return score_id

	def get_all(self):
		return self.collection.find({})

	def delete(self, obj_to_delete):
		if not isinstance(obj_to_delete, DBObject):
			raise TypeError("Expected DBObject")
		if not obj_to_delete.is_id_set():
			raise AttributeError("DBObject needs to have an id in order to be deleted")
		self.collection.remove({'_id': obj_to_delete.get_id()})

	def delete_all(self):
		self.collection.remove({})


class DBScoreWorker(DBWorker):
	def __init__(self):
		DBWorker.__init__(self)
		self.db = self.client.spacekatz
		self.collection = self.db.scores

	def get_all(self):
		return self.collection.find({}).sort("points", DESCENDING)





