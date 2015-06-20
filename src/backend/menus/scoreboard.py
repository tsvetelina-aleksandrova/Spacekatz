import json
from backend.menus.score import Score
from backend.db.db_worker import DBScoreWorker


class Scoreboard:
    def __init__(self, db_worker=""):
        self.__type_err_msg = "Only Score elements can be added to Scoreboard"
        if db_worker:
            self.db_score_worker = db_worker
        else:
            self.db_score_worker = DBScoreWorker()

    def add(self, score):
        if not isinstance(score, Score):
            raise TypeError(self.__type_err_msg)
        new_score_id = self.db_score_worker.create(score)
        score.set_id(new_score_id)

    def get_all(self):
        scores_list = []
        scores_dict = self.db_score_worker.get_all()
        for score_info in scores_dict:
            score_obj = Score(score_info["player"], score_info["points"])
            score_obj.set_id(score_info["_id"])
            scores_list.append(score_obj)
        return scores_list

    def delete_all(self):
        self.db_score_worker.delete_all()

    def delete(self, score_to_delete):
        if not isinstance(score_to_delete, Score):
            raise TypeError(self.__type_err_msg)
        self.db_score_worker.delete(score_to_delete)

    def display(self):
        scores_list = self.get_all()
        for score in scores_list:
            print(score)
