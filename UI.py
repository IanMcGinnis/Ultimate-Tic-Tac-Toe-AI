from constraints import *


def show_lines():
    # vertical lines for big board
    pygame.draw.line(line_screen, LINE_COLOR, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(line_screen, LINE_COLOR, (SQSIZE * 2, 0), (SQSIZE * 2, HEIGHT), LINE_WIDTH)
    # vertical lines for tiny boards
    # col 1
    pygame.draw.line(line_screen, LINE_COLOR, (SQSIZE * 1 / 3, 0), (SQSIZE * 1 / 3, HEIGHT), TINY_LINE_WIDTH)
    pygame.draw.line(line_screen, LINE_COLOR, (SQSIZE * 2 / 3, 0), (SQSIZE * 2 / 3, HEIGHT), TINY_LINE_WIDTH)
    # col 2
    pygame.draw.line(line_screen, LINE_COLOR, (SQSIZE * 4 / 3, 0), (SQSIZE * 4 / 3, HEIGHT), TINY_LINE_WIDTH)
    pygame.draw.line(line_screen, LINE_COLOR, (SQSIZE * 5 / 3, 0), (SQSIZE * 5 / 3, HEIGHT), TINY_LINE_WIDTH)
    # col 3
    pygame.draw.line(line_screen, LINE_COLOR, (SQSIZE * 7 / 3, 0), (SQSIZE * 7 / 3, HEIGHT), TINY_LINE_WIDTH)
    pygame.draw.line(line_screen, LINE_COLOR, (SQSIZE * 8 / 3, 0), (SQSIZE * 8 / 3, HEIGHT), TINY_LINE_WIDTH)

    # horizontal lines
    pygame.draw.line(line_screen, LINE_COLOR, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)
    pygame.draw.line(line_screen, LINE_COLOR, (0, SQSIZE * 2), (WIDTH, SQSIZE * 2), LINE_WIDTH)
    # horizontal lines for tiny boards
    # row 1
    pygame.draw.line(line_screen, LINE_COLOR, (0, SQSIZE * 1 / 3), (WIDTH, SQSIZE * 1 / 3), TINY_LINE_WIDTH)
    pygame.draw.line(line_screen, LINE_COLOR, (0, SQSIZE * 2 / 3), (WIDTH, SQSIZE * 2 / 3), TINY_LINE_WIDTH)
    # row 2
    pygame.draw.line(line_screen, LINE_COLOR, (0, SQSIZE * 4 / 3), (WIDTH, SQSIZE * 4 / 3), TINY_LINE_WIDTH)
    pygame.draw.line(line_screen, LINE_COLOR, (0, SQSIZE * 5 / 3), (WIDTH, SQSIZE * 5 / 3), TINY_LINE_WIDTH)
    # row 3
    pygame.draw.line(line_screen, LINE_COLOR, (0, SQSIZE * 7 / 3), (WIDTH, SQSIZE * 7 / 3), TINY_LINE_WIDTH)
    pygame.draw.line(line_screen, LINE_COLOR, (0, SQSIZE * 8 / 3), (WIDTH, SQSIZE * 8 / 3), TINY_LINE_WIDTH)


def draw_active_area(row, col):
    active_screen.fill(BG_COLOR)
    pygame.draw.rect(active_screen, ACTIVE_COLOR, pygame.Rect(col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE))

def draw_fig(row, col, player):
    if player == CROSS:
        start_desc = (col * SMALL_SQIZE + 15, row * SMALL_SQIZE + 15)
        end_desc = (col * SMALL_SQIZE + SMALL_SQIZE - 15, row * SMALL_SQIZE + SMALL_SQIZE - 15)
        pygame.draw.line(play_screen, CROSS_COLOR, start_desc, end_desc, TINY_LINE_WIDTH)

        start_asc = (col * SMALL_SQIZE + 15, row * SMALL_SQIZE + SMALL_SQIZE - 15)
        end_asc = (col * SMALL_SQIZE + SMALL_SQIZE - 15, row * SMALL_SQIZE + 15)
        pygame.draw.line(play_screen, CROSS_COLOR, start_asc, end_asc, TINY_LINE_WIDTH)

    elif player == CIRCLE:
        center = (col * SMALL_SQIZE + SMALL_SQIZE // 2, row * SMALL_SQIZE + SMALL_SQIZE // 2)
        pygame.draw.circle(play_screen, CIRC_COLOR, center, TINY_RADIUS, TINY_CIRC_WIDTH)
    line_screen.blit(play_screen, (0, 0))

def draw_large_fig(row, col, player):
    if player == 1:
        start_desc = ((col - 1) * SQSIZE + OFFSET, (row - 1) * SQSIZE + OFFSET)
        end_desc = ((col - 1) * SQSIZE + SQSIZE - OFFSET, (row - 1) * SQSIZE + SQSIZE - OFFSET)
        pygame.draw.line(play_screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

        start_asc = ((col - 1) * SQSIZE + OFFSET, (row - 1) * SQSIZE + SQSIZE - OFFSET)
        end_asc = ((col - 1) * SQSIZE + SQSIZE - OFFSET, (row - 1) * SQSIZE + OFFSET)
        pygame.draw.line(play_screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

    elif player == 2:
        center = ((col - 1) * SQSIZE + SQSIZE // 2, (row - 1) * SQSIZE + SQSIZE // 2)
        pygame.draw.circle(play_screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)
    line_screen.blit(play_screen, (0, 0))


