import pygame

WIDTH = 900
HEIGHT = 900

ROWS = 3
COLS = 3
SQSIZE = WIDTH // ROWS # = 300

SMALL_SQIZE = SQSIZE // ROWS # = 100

LINE_WIDTH = 18
CIRC_WIDTH = 27
CROSS_WIDTH = 20
RADIUS = SQSIZE // 3
TINY_LINE_WIDTH = 9
TINY_CIRC_WIDTH = 9
TINY_RADIUS = SMALL_SQIZE // 3

OFFSET = 50

#colors
BG_COLOR = (28, 170, 156)
ACTIVE_COLOR = (56, 255, 255)
LINE_COLOR = (23, 145, 135)
LOCAL_WIN_COLOR = (127, 127, 127 )
CIRC_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

#player number
CROSS = 1
CIRCLE = 2

#pygame global initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
line_screen = screen.subsurface(0, 0, WIDTH, HEIGHT)
active_screen = screen.subsurface(0, 0, WIDTH, HEIGHT)

play_screen = pygame.surface.Surface((WIDTH, HEIGHT))
play_screen.set_colorkey((0, 0, 0))

pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOR)