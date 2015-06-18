import unittest
import mock
import sys
import os
sys.path.append(os.path.join('..\..', 'src'))

from backend.menus.scoreboard import Scoreboard
from backend.menus.score import Score


class ScoreboardTest(unittest.TestCase):
    @mock.patch('backend.db.db_worker.DBScoreWorker')
    def setUp(self, mock_db_worker):
        self.score = Score("Test1", 10)
        self.score2 = Score("Test2", 20)

        self.mock_db_worker = mock_db_worker
        self.scoreboard = Scoreboard(mock_db_worker)

        self.db_data = [
            {
                "player": "Test1",
                "points": 10,
                "_id": "1"
            },
            {
                "player": "Test2",
                "points": 20,
                "_id": "2"
            }]

    def test_add_score(self):
        score_id = "1234"
        self.mock_db_worker.create.return_value = score_id
        self.scoreboard.add(self.score)

        self.assertTrue(self.mock_db_worker.create.called)
        self.assertEqual(self.score.get_id(), score_id)

    def test_get_all(self):
        self.mock_db_worker.get_all.return_value = self.db_data
        returned_scores = self.scoreboard.get_all()

        self.assertTrue(self.mock_db_worker.get_all.called)
        self.assertEqual(len(returned_scores), 2)

        self.assertEqual(returned_scores[0].get_player_name(),
                         self.score.get_player_name())
        self.assertEqual(returned_scores[1].get_player_name(),
                         self.score2.get_player_name())

        self.assertEqual(returned_scores[0].get_points(),
                         self.score.get_points())
        self.assertEqual(returned_scores[1].get_points(),
                         self.score2.get_points())

    def test_delete_all(self):
        self.scoreboard.delete_all()
        self.assertTrue(self.mock_db_worker.delete_all.called)

    def test_delete_score(self):
        self.scoreboard.delete(self.score)
        self.assertTrue(self.mock_db_worker.delete.called)


if __name__ == '__main__':
    unittest.main()
