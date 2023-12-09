from constraints import *
from MCTS import *
class AI:
    def __init__(self, player, level):
        self.level = level
        self.player = player

    def rnd(self, board, activeBoardRow, activeBoardCol):
        empty_sqrs = board.squares[activeBoardRow][activeBoardCol].get_empty_sqrs()

        while(len(empty_sqrs) == 0 or board.squares[activeBoardRow][activeBoardCol].local_final_state() != 0):

            activeBoardRow = random.randrange(0, ROWS)
            activeBoardCol = random.randrange(0, COLS)
            empty_sqrs = board.squares[activeBoardRow][activeBoardCol].get_empty_sqrs()

        idx = random.randrange(0, len(empty_sqrs))
        move = empty_sqrs[idx]
        return move[0], move[1], activeBoardRow, activeBoardCol


    def eval(self, main_board, activeBoardRow, activeBoardCol):
        if self.level == 0:
            #random choice
            eval = 'random'
            row, col, activeBoardRow, activeBoardCol  = self.rnd(main_board, activeBoardRow, activeBoardCol)
        else:
            #Monti Carlo Tree Search algorithm choice
            (row, col, activeBoardRow, activeBoardCol), eval = mcts(main_board, activeBoardRow, activeBoardCol, self.player)
        print(f'AI: {self.player} has chosen to mark the square in pos ({row}, {col}) with an eval of: {eval}')
        return row, col, activeBoardRow, activeBoardCol #row, col
