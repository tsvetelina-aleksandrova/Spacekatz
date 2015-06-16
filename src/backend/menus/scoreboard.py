import json
from sources.backend.score import Score
from sources.backend.db.db_worker import DBScoreWorker

class Scoreboard:

	def __init__(self):
		self.__type_err_msg = "Addition to scoreboard expects Score elements"
		self.db_score_worker = DBScoreWorker()

	def add(self, score):
		if not isinstance(score, Score):
			raise TypeError(self.__type_err_msg)
		new_score_id = self.db_score_worker.create(score)
		score.set_id(new_score_id)
			
	def get_all(self):
		scores_list = []
		scores_json = self.db_score_worker.get_all()
		for score_map in scores_json:
			score_obj = Score(score_map["user"], score_map["points"])
			score_obj.set_id(score_map["_id"])
			scores_list.append(score_obj)
		return scores_list

	def delete_all(self):
		self.db_score_worker.delete_all()

	def delete(self, score_to_delete):
		if not isinstance(score_to_delete, Score):
			raise TypeError(self.__type_err_msg)
		self.db_score_worker.delete(score_to_delete)

		