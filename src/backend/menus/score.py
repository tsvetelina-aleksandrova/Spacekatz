from sources.backend.db.db_obj import DBObject

class Score(DBObject):
	def __init__(self, player_name, points):
		DBObject.__init__(self)
		self.__player_name = player_name
		self.__points = points

	def get_player_name(self):
		return self.__player_name

	def get_points(self):
		return self.__points

	def increase_score(self, points):
		self.__points += points

	def get_as_map(self):
		return {
			"user": self.get_player_name(),
			"points": self.get_points()
			}

	def __eq__(self, other):
		if not type(self) == type(other):
			err_msg = 'Comparing objects of type {} and {}'.format(
				type(self), type(other))
			raise ValueError(err_msg)
		if self.is_id_set() and other.is_id_set():
			return self.get_id() == other.get_id()
		err_msg = "Scores should have ids in order to be compared"
		raise AttributeError(err_msg)

	def __str__(self):
		return " ".join([
			"Player:", 
			self.__player_name, 
			"Score:", 
			str(self.__points)])