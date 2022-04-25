import pygame, sys
import numpy as np

# variable
pygame.init()
WIDTH = 600
HEIGHT = 600
board_row = 3
board_col = 3
background_color = (28, 170, 0)
player=1

# screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(background_color)

# board
board = np.zeros((board_row, board_col))

print(board)


# drawboard
def drawborderline(start, end):
    pygame.draw.line(screen, (255, 255, 255), start, end, 5)


vertical_line_start = ((0, 200), (0, 400))
vertical_line_end = ((600, 200), (600, 400))
horizontal_line_start = ((200, 0), (400, 0))
horizontal_line_end = ((200, 600), (400, 600))

for start in range(len(vertical_line_start)):
    for end in range(len(vertical_line_end)):
        if start == end:
            drawborderline(vertical_line_start[start], vertical_line_end[end])

for start in range(len(horizontal_line_start)):
    for end in range(len(horizontal_line_end)):
        if start == end:
            drawborderline(horizontal_line_start[start], horizontal_line_end[end])

#Mark when player click
def mark_when_player_click(row,col):
    board[row][col]=player

# drawo
def drawo_out(cen, ra):
    pygame.draw.circle(screen, (255, 255, 255), cen, ra)

def drawo_in(cen, ra, colr):
    pygame.draw.circle(screen, colr, cen, ra)


# drawx
def drawx(start, end):
    pygame.draw.line(screen, (0, 0, 0), start, end, 10)
    pygame.draw.line(screen, (0, 0, 0), start, end, 10)

#draw after player click
def drawo_after_click(pos):
    global player
    #drawo in row 1
    if pos[0] > 0 and pos[1] > 0 and pos[0] <= 197 and pos[1]<= 197 and board[0][0] == 0:
        drawo_out((197 / 2, 197 / 2), 190 / 2)
        drawo_in((197 / 2, 197 / 2), 180 / 2, background_color)
        mark_when_player_click(0,0)
        print(board)
        player=2

    if pos[0] > 203 and pos[1] > 0 and pos[0] <= 397 and pos[1]<= 197 and board[0][1] == 0:
        drawo_out((397 - 190 / 2, 197 / 2), 190 / 2)
        drawo_in((397 - 190 / 2, 197 / 2), 180 / 2, background_color)
        mark_when_player_click(0,1)
        print(board)
        player = 2

    if pos[0] > 403 and pos[1] > 0 and pos[0] <= 600 and pos[1]<= 197 and board[0][2] == 0:
        drawo_out((600 - 197 / 2, 197 / 2), 190 / 2)
        drawo_in((600 - 197 / 2, 197 / 2), 180 / 2, background_color)
        mark_when_player_click(0,2)
        print(board)
        player = 2

    # #drawo in row 2
    if pos[0] > 0 and pos[1] > 203 and pos[0] <= 197 and pos[1]<= 397 and board[1][0] == 0:
        drawo_out((197 / 2, 397 - 190 / 2), 190 / 2)
        drawo_in((197 / 2, 397 - 190 / 2), 180 / 2, background_color)
        mark_when_player_click(1,0)
        print(board)
        player=2

    if pos[0] > 203 and pos[1] > 203 and pos[0] <= 397 and pos[1]<= 397 and board[1][1] == 0:
        drawo_out((397 - 190 / 2, 397 - 190 / 2), 190 / 2)
        drawo_in((397 - 190 / 2, 397 - 190 / 2), 180 / 2, background_color)
        mark_when_player_click(1,1)
        print(board)
        player = 2

    if pos[0] > 403 and pos[1] > 203 and pos[0] <= 600 and pos[1]<= 397 and board[1][2] == 0:
        drawo_out((600 - 197 / 2, 397 - 190 / 2), 190 / 2)
        drawo_in((600 - 197 / 2, 397 - 190 / 2), 180 / 2, background_color)
        mark_when_player_click(1,2)
        print(board)
        player = 2

    # #drawo in row 3
    if pos[0] > 0 and pos[1] > 403 and pos[0] <= 197 and pos[1]<= 600 and board[2][0] == 0:
        drawo_out((197 / 2, 600 - 197 / 2), 190 / 2)
        drawo_in((197 / 2, 600 - 197 / 2), 180 / 2, background_color)
        mark_when_player_click(2,0)
        print(board)
        player=2

    if pos[0] > 203 and pos[1] > 403 and pos[0] <= 397 and pos[1]<= 600 and board[2][1] == 0:
        drawo_out((397 - 190 / 2, 600 - 197 / 2), 190 / 2)
        drawo_in((397 - 190 / 2, 600 - 197 / 2), 180 / 2, background_color)
        mark_when_player_click(2,1)
        print(board)
        player = 2

    if pos[0] > 403 and pos[1] > 403 and pos[0] <= 600 and pos[1]<= 600 and board[2][2] == 0:
        drawo_out((600 - 197 / 2, 600 - 197 / 2), 190 / 2)
        drawo_in((600 - 197 / 2, 600 - 197 / 2), 180 / 2, background_color)
        mark_when_player_click(2,2)
        print(board)
        player = 2

def drawx_after_click(pos):
    global player
    #drawo in row 1
    if pos[0] > 0 and pos[1] > 0 and pos[0] <= 197 and pos[1]<= 197 and board[0][0] == 0:
        drawx((10,10), (197-10,197-10))
        drawx((10,197-10), (197 - 10, 10))
        mark_when_player_click(0,0)
        print(board)
        player=1

    if pos[0] > 203 and pos[1] > 0 and pos[0] <= 397 and pos[1]<= 197 and board[0][1] == 0:
        drawx((203+10, 0+10), (397 - 10, 197 - 10))
        drawx((203+10, 197 - 10), (397 - 10, 0+10))
        mark_when_player_click(0,1)
        print(board)
        player = 1

    if pos[0] > 403 and pos[1] > 0 and pos[0] <= 600 and pos[1]<= 197 and board[0][2] == 0:
        drawx((403 + 10, 0 + 10), (600 - 10, 197 - 10))
        drawx((403 + 10, 197 - 10), (600 - 10, 0 + 10))
        mark_when_player_click(0,2)
        print(board)
        player = 1

    # #drawo in row 2
    if pos[0] > 0 and pos[1] > 203 and pos[0] <= 197 and pos[1]<= 397 and board[1][0] == 0:
        drawx((0 + 10, 203 + 10), (197 - 10, 397 - 10))
        drawx((0 + 10, 397 - 10), (197 - 10, 203 + 10))
        mark_when_player_click(1,0)
        print(board)
        player=1

    if pos[0] > 203 and pos[1] > 203 and pos[0] <= 397 and pos[1]<= 397 and board[1][1] == 0:
        drawx((203 + 10, 203 + 10), (397 - 10, 397 - 10))
        drawx((203 + 10, 397 - 10), (397 - 10, 203 + 10))
        mark_when_player_click(1,1)
        print(board)
        player = 1

    if pos[0] > 403 and pos[1] > 203 and pos[0] <= 600 and pos[1]<= 397 and board[1][2] == 0:
        drawx((403 + 10, 203 + 10), (600 - 10, 397 - 10))
        drawx((403 + 10, 397 - 10), (600 - 10, 203 + 10))
        mark_when_player_click(1,2)
        print(board)
        player = 1

    # #drawo in row 3
    if pos[0] > 0 and pos[1] > 403 and pos[0] <= 197 and pos[1]<= 600 and board[2][0] == 0:
        drawx((0 + 10, 403 + 10), (197 - 10, 600 - 10))
        drawx((0 + 10, 600 - 10), (197 - 10, 403 + 10))
        mark_when_player_click(2,0)
        print(board)
        player=1

    if pos[0] > 203 and pos[1] > 403 and pos[0] <= 397 and pos[1]<= 600 and board[2][1] == 0:
        drawx((203 + 10, 403 + 10), (397 - 10, 600 - 10))
        drawx((203 + 10, 600 - 10), (397 - 10, 403 + 10))
        mark_when_player_click(2,1)
        print(board)
        player = 1

    if pos[0] > 403 and pos[1] > 403 and pos[0] <= 600 and pos[1]<= 600 and board[2][2] == 0:
        drawx((403 + 10, 403 + 10), (600 - 10, 600 - 10))
        drawx((403 + 10, 600 - 10), (600 - 10, 403 + 10))
        mark_when_player_click(2,2)
        print(board)
        player = 1


# run_the_game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.ext()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if player == 1:
                drawo_after_click(pos)
            #print(pos)
            elif player == 2:
                drawx_after_click(pos)

    # check win of row
    if board[0][0] == board[0][1] and board[0][1] == board [0][2] and board[0][1] != 0:
        pygame.draw.line(screen,(255,255,255),(0, 197 / 2),(600, 197 / 2),10)
    if board[1][0] == board[1][1] and board[1][1] == board [1][2] and board[1][1] != 0:
        pygame.draw.line(screen,(255,255,255),(0, 397- 197 / 2),(600, 397-197 / 2),10)
    if board[2][0] == board[2][1] and board[2][1] == board [2][2] and board[2][1] != 0:
        pygame.draw.line(screen,(255,255,255),(0, 600-197 / 2),(600, 600-197 / 2),10)

    # check win of col
    if board[0][0] == board[1][0] and board[1][0] == board [2][0] and board[1][0] != 0:
        pygame.draw.line(screen,(255,255,255),(197/2, 0),(197 / 2, 600),10)
    if board[0][1] == board[1][1] and board[1][1] == board [2][1] and board[1][1] != 0:
        pygame.draw.line(screen,(255,255,255),(397- 197 / 2, 0),(397-197 / 2,600),10)
    if board[0][2] == board[1][2] and board[1][2] == board [2][2] and board[1][2] != 0:
        pygame.draw.line(screen,(255,255,255),(600-197 / 2, 0),(600-197 / 2,600),10)

    # check win of x
    if board[0][0] == board[1][1] and board[1][1] == board [2][2] and board[1][1] != 0:
        pygame.draw.line(screen,(255,255,255),(0, 0),(600, 600),10)
    if board[0][2] == board[1][1] and board[1][1] == board [2][0] and board[1][1] != 0:
        pygame.draw.line(screen,(255,255,255),(0, 600),(600, 0),10)

    pygame.display.update()
