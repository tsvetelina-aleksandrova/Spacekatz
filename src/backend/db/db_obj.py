class DBObject:
	def __init__(self):
		self.__id = None

	def set_id(self, id):
		self.__id = id

	def is_id_set(self):
		return not type(self.__id) == None

	def get_id(self):
		return self.__id
		
	def get_as_map(self):
		pass