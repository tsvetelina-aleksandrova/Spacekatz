def Score(DBObject):
	def __init__(self, user_name, points):
		DBObject.__init__(self)
		self.__user_name = user_name
		self.__points = points

	def get_user_name(self):
		return self.__user_name

	def get_points(self):
		return self.__points

	def increase_score(self, points):
		self.__points += points

	def get_as_map(self):
		return {
			"user": self.get_user_name(),
			"points": self.get_points()
			}

	def __eq__(self, other):
    	if type(self) != type(other):
    		err_msg = 'Comparing objects of type {} and {}'.format(
    			type(self), type(other))
        	raise ValueError(err_msg)
        if self.is_id_set() and other.is_id_set()
    		return self.get_id() = other.get_id()
    	err_msg = "Scores should have ids in order to be compared"
    	raise AttributeError(err_msg)

	def __str__(self):
		return " ".join([
			"User:", 
			self.__user_name, 
			"Score:", 
			self.__points])