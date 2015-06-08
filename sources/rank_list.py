def RankList:
	from score import Score
	from db_worker import DBScoreWorker

	def __init__(self):
		# self.list = []
		self.__type_err_msg = "Addition to ranklist expects Score elements"
		self.db_score_worker = DBScoreWorker()

	def add_score(self, score)
		if not isinstance(score, score.Score):
			raise TypeError(self.__type_err_msg)
		new_score_id = self.db_score_worker.create(score)
		score.set_id(new_score_id)
		# list.append(score)
			
	def get_scores(self):
		# return sorted(self.list, key=lambda score: score.get_points())
		scores_list = []
		scores_json = self.db_score_worker.get_all()
		for score_map in json.loads(scores_json):
			score_obj = Score(score_map.user, score_map.points)
			score_obj.set_id(score_map.["_id"])
			scores_list.append(score_obj)
		return scores_list

	def delete_all_scores(self):
		# self.list = []
		self.db_score_worker.delete_all()

	def delete_score(self, score_to_delete):
		if not isinstance(score, score.Score):
			raise TypeError(self.__type_err_msg)
		# self.list = [score for score in self.list if not score == score_to_delete]
		self.db_score_worker.delete(score)