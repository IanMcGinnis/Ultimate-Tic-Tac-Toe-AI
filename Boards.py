import copy
import numpy as np
from UI import *

class Wide_Board:
    def __init__(self):
        # creates a list of local tic-tac-toe boards
        self.squares = [[Local_Board(1, 1), Local_Board(1, 2), Local_Board(1, 3)],
                        [Local_Board(2, 1), Local_Board(2, 2), Local_Board(2, 3)],
                        [Local_Board(3, 1), Local_Board(3, 2), Local_Board(3, 3)]]

        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def final_state(self, show = False):
        #vertical wins
        for col in range(COLS):
            if self.squares[0][col].local_final_state() == self.squares[1][col].local_final_state() == self.squares[2][col].local_final_state() != 0:
                if show:
                    color = CIRC_COLOR if self.squares[0][col].local_final_state() == 2 else CROSS_COLOR
                    iPos = (col * SQSIZE + SQSIZE // 2, 20)
                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[0][col].local_final_state()
        #horizontal wins
        for row in range(ROWS):
            if self.squares[row][0].local_final_state() == self.squares[row][1].local_final_state() == self.squares[row][2].local_final_state() != 0:
                if show:
                    color = CIRC_COLOR if self.squares[row][0].local_final_state() == 2 else CROSS_COLOR
                    iPos = (20, row * SQSIZE + SQSIZE // 2)
                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)
                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
                return self.squares[row][0].local_final_state()

        #diagnal wins
        if self.squares[0][0].local_final_state() == self.squares[1][1].local_final_state() == self.squares[2][2].local_final_state() != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1].local_final_state() == 2 else CROSS_COLOR
                iPos = (20, 20)
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
            return self.squares[1][1].local_final_state()
        if self.squares[2][0].local_final_state() == self.squares[1][1].local_final_state() == self.squares[0][2].local_final_state() != 0:
            if show:
                color = CIRC_COLOR if self.squares[1][1].local_final_state() == 2 else CROSS_COLOR
                iPos = (20, HEIGHT - 20)
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)
            return self.squares[1][1].local_final_state()

        #no win
        return 0

    def get_legal_moves(self):
        legal_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                if not self.is_large_sqr_full() and self.empty_large_sqr(row, col) and self.squares[row][col].local_final_state() == 0:
                    empty_small_squares = self.squares[row][col].get_empty_sqrs()
                    legal_moves.extend(
                        [(row, col, small_row, small_col) for (small_row, small_col) in empty_small_squares])
        return legal_moves

    def is_terminal(self):
        # Check if the current state is a terminal state
        return self.final_state(show = True) != 0 or self.is_large_sqr_full()

    def apply_move(self, move, player, mcts = False):
        # Apply a given move to the current state
        row, col, activeBoardRow, activeBoardCol = move
        self.squares[activeBoardRow][activeBoardCol].mark_sqr(row, col, player)
        if not mcts:
            draw_fig(row + ROWS * activeBoardRow, col + COLS * activeBoardCol, player)
        self.update(row, col)

    def update(self, row, col):
        screen.fill(BG_COLOR)
        draw_active_area(row, col)
        show_lines()
        line_screen.blit(play_screen, (0, 0))

    def copy(self):
        # Create a copy of the current state
        copied_board = copy.deepcopy(self)
        #disables the drawing function to avoid showing player when algorithm is working
        setattr(copied_board, 'draw_large_fig', None)
        return copied_board

    def find_empty_small_sqr(self, row, col):
        return self.squares[row][col].get_empty_sqrs()

    def empty_large_sqr(self, row, col):
        return self.squares[row//ROWS][col//COLS].empty_sqr(row % ROWS, col % COLS)

    def is_large_sqr_full(self):
        return self.marked_sqrs == 9


class Local_Board:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.squares = np.zeros((ROWS, COLS))
        self.empty_sqrs = self.squares
        self.marked_sqrs = 0

    def local_final_state(self):
        #vertical wins
        for col in range(COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                iPos = (self.col * SQSIZE + col * SMALL_SQIZE + SMALL_SQIZE // 2 - SQSIZE, self.row * SQSIZE + 20 - SQSIZE)
                fPos = (self.col * SQSIZE + col * SMALL_SQIZE + SMALL_SQIZE // 2 - SQSIZE, self.row * SQSIZE - 20)
                pygame.draw.line(active_screen, LOCAL_WIN_COLOR, iPos, fPos, LINE_WIDTH)
                #TODO
                # REMOVE DRAW LARGE AND MAKE A CALL TO UI AFTER THIS HAS BEEN DONE
                draw_large_fig(self.row, self.col, self.squares[0][col])
                return self.squares[0][col]
        #horizontal wins
        for row in range(ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                iPos = (self.col * SQSIZE + 20 - SQSIZE, self.row * SQSIZE + row * SMALL_SQIZE + SMALL_SQIZE // 2 - SQSIZE)
                fPos = (self.col * SQSIZE - 20, self.row * SQSIZE + row * SMALL_SQIZE + SMALL_SQIZE // 2 - SQSIZE)
                pygame.draw.line(screen, LOCAL_WIN_COLOR, iPos, fPos, LINE_WIDTH)
                draw_large_fig(self.row, self.col, self.squares[row][0])
                return self.squares[row][0]

        #diagnal wins
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            iPos = (self.col * SQSIZE - SQSIZE + 30, self.row * SQSIZE + 30 - SQSIZE)
            fPos = (self.col * SQSIZE - 30, self.row * SQSIZE - 30)
            pygame.draw.line(screen, LOCAL_WIN_COLOR, iPos, fPos, LINE_WIDTH)
            draw_large_fig(self.row, self.col, self.squares[1][1])
            return self.squares[1][1]
        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            iPos = (self.col * SQSIZE - 30, self.row * SQSIZE - SQSIZE + 30)
            fPos = (self.col * SQSIZE - SQSIZE + 30, self.row * SQSIZE - 30)
            pygame.draw.line(screen, LOCAL_WIN_COLOR, iPos, fPos, LINE_WIDTH)
            draw_large_fig(self.row, self.col, self.squares[1][1])
            return self.squares[1][1]

        #no win
        return 0


    def mark_sqr(self, row, col, player):
        self.squares[row][col] = player
        self.marked_sqrs += 1
    def empty_sqr(self, row, col):
        return self.squares[row][col] == 0

    def get_empty_sqrs(self):
        empty_sqrs = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.empty_sqr(row, col):
                    empty_sqrs.append((row, col))

        return empty_sqrs

    def isfull(self):
        return  self.marked_sqrs == 9

    def isempty(self):
        return self.marked_sqrs == 0

