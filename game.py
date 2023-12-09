import sys
import time

from Boards import Wide_Board, Local_Board
from UI import *
from constraints import *
from Players import AI

class Game:
    def __init__(self):
        self.board = Wide_Board()
        self.ai1 = AI(CROSS, 0)
        self.ai2 = AI(CIRCLE, 1)
        self.player = CROSS
        self.gamemode = 'ai'  # pvp or ai
        self.running = True
        show_lines()

    def reset(self):
        self.board.squares.clear()
        self.board.squares = [[Local_Board(1, 1), Local_Board(1, 2), Local_Board(1, 3)],
                              [Local_Board(2, 1), Local_Board(2, 2), Local_Board(2, 3)],
                              [Local_Board(3, 1), Local_Board(3, 2), Local_Board(3, 3)]]
        self.board.empty_sqrs = self.board.squares
        self.board.marked_sqrs = 0
        self.running = True
        self.player = 1

        screen.fill(BG_COLOR)
        play_screen.fill((0, 0 ,0))
        show_lines()

    def playerMove(self):
        if self.player == CROSS:
            self.player = CIRCLE
        else:
            self.player = CROSS

    def isover(self):
        return self.board.final_state(show = True) != 0 or self.board.is_large_sqr_full()
def main():

    game = Game()
    ai = game.ai1
    ai2 = game.ai2
    board = game.board
    active_board_row = 1
    active_board_col = 1

    while True:
        if game.isover() == True:
            print("game  over \n")
            time.sleep(3)
            game.reset()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #TODO
            # Replace this event with AI and comment out AI
            '''
             #Human interaction
            if event.type == pygame.MOUSEBUTTONDOWN:
                 pos = event.pos
                 row = pos[1] // SMALL_SQIZE
                 col = pos[0] // SMALL_SQIZE

                 activeBoardRow = row % ROWS
                 activeBoardCol = col % COLS

                 # human mark sqr
                 if board.empty_large_sqr(row, col) and game.running:
                     #print()
                     game.draw_fig(row, col)
                     board.mark_sqr(row, col, 1)
                     game.next_turn()
                     if game.isover():
                            game.running = False
            '''
        if game.gamemode == 'ai' and game.player == CROSS and game.running:
            pygame.display.update()
            move = ai.eval(board, active_board_row, active_board_col)

            board.apply_move(move, CROSS, False)

            row = move[0]
            col = move[1]
            active_board_row, active_board_col = row, col
            game.playerMove()

        pygame.display.update()
        time.sleep(1)

        if game.gamemode == 'ai' and game.player == CIRCLE and game.running:
            pygame.display.update()
            move = ai2.eval(board, active_board_row, active_board_col)

            board.apply_move(move, CIRCLE, False)

            row = move[0]
            col = move[1]
            active_board_row, active_board_col = row, col
            game.playerMove()

        pygame.display.update()
        time.sleep(1)

if __name__ == '__main__':
    main()
