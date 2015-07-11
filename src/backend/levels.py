from backend.util.board import Board
from backend.sprites.bird_init_pos import SingleBlockInitPos
from backend.sprites.bird_init_pos import DiagInitPos
from backend.sprites.bird_init_pos import BlockInitPos
from backend.sprites.bird_init_pos import SingleInitPos
from backend.sprites.bird_move_strategies import InPlaceStrategy
from backend.sprites.bird_move_strategies import DiagonalStrategy
from backend.sprites.bird_move_strategies import BlockStrategy
from backend.sprites.bird_move_strategies import BossStrategy
from ui.sprites.bird_ui import Bird


class Level():

    def __init__(self, board, lvl):
        if lvl < 0:
            lvl = 0
        if lvl > 5:
            lvl = 5
        self.lvl = lvl
        self.board = board
        self.enemy_nums = [3, 2, 2, 3, 1]

    def get_enemies(self):
        # the configuration of enemies and their
        # initial positions, movement abilities and strengths
        # is level-specific
        diag_dirs = [
            DiagonalStrategy.directions[2],
            DiagonalStrategy.directions[1]
        ]
        self.enemy_strategies = [
            InPlaceStrategy(),
            DiagonalStrategy(diag_dirs[0]),
            DiagonalStrategy(diag_dirs[1]),
            BlockStrategy(),
            BossStrategy()
        ]
        self.enemy_init_pos = [
            SingleBlockInitPos(),
            DiagInitPos(20, diag_dirs[0]),
            DiagInitPos(20, diag_dirs[1]),
            BlockInitPos(),
            SingleInitPos()
        ]

        # hmmm
        self.lvl = 0
        enemies = []
        strategy = self.enemy_strategies[self.lvl]

        for i in range(self.enemy_nums[self.lvl]):
            current_bird_init_pos = next(self.enemy_init_pos[self.lvl])
            new_bird = Bird(current_bird_init_pos, strategy, self.board)
            enemies.append(new_bird)
        return enemies
