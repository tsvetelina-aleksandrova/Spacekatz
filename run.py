import sources.game
from sources.rank_list import RankList
from sources.score import Score

sources.game.play()

"""
list = RankList()
score1 = Score("test1", 1)
score2 = Score("test2", 2)
score3 = Score("test3", 3)
list.add(score1)
list.add(score2)
for s in list.get_all():
	print(s)

list.delete(score1)
for s in list.get_all():
	print(s)

list.add(score3)
for s in list.get_all():
	print(s)
list.delete_all()
"""