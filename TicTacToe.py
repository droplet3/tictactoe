import pygame as p
from pygame.locals import *

p.init()

# Constants:
WIDTH, HEIGHT = 300, 300
WINDOW = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("Tic Tac Toe")

# Colors:
BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
GREY = (122, 122, 122)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BACKGROUND_COLOR = WHITE
OUTLINE_COLOR = BLACK
OUTLINE_THICKNESS = 5
FONT = p.font.SysFont("comicsans", 30)

clicked = False
player = 1
pos = (0,0)
location = []
game_over = False
winner = 0
replay_box = Rect(WIDTH // 2 - 80, HEIGHT // 2, 160, 50)

for x in range(3):
    row = [0] * 3
    location.append(row)

def draw_grid():
    WINDOW.fill(BACKGROUND_COLOR)
    grid = OUTLINE_COLOR
    for x in range(1,3):
        p.draw.line(WINDOW, grid, (0, 100 * x), (WIDTH,100 * x), OUTLINE_THICKNESS) #horizontal lines
        p.draw.line(WINDOW, grid, (100 * x, 0), (100 * x, HEIGHT), OUTLINE_THICKNESS) #vertical lines

def draw_location():
    x_pos = 0
    for x in location:
        y_pos = 0
        for y in x:
            if y == 1:
                p.draw.line(WINDOW, GREEN, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), OUTLINE_THICKNESS)
                p.draw.line(WINDOW, GREEN, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), OUTLINE_THICKNESS)
            if y == -1:
                p.draw.circle(WINDOW, RED, (x_pos * 100 + 50, y_pos * 100 + 50), 38, OUTLINE_THICKNESS)
            y_pos += 1
        x_pos += 1

def check_game_over():
    global game_over, winner
    x_pos = 0
    for x in location:
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        if location[0][x_pos] + location [1][x_pos] + location [2][x_pos] == 3:
            winner = 1
            game_over = True
        if location[0][x_pos] + location [1][x_pos] + location [2][x_pos] == -3:
            winner = 2
            game_over = True
        x_pos += 1

    if location[0][0] + location[1][1] + location [2][2] == 3 or location[2][0] + location[1][1] + location [0][2] == 3:
        winner = 1
        game_over = True
    if location[0][0] + location[1][1] + location [2][2] == -3 or location[2][0] + location[1][1] + location [0][2] == -3:
        winner = 2
        game_over = True

    # Check if Tied
    if not game_over:
        tie = True
        for row in location:
            for i in row:
                if i == 0:
                    tie = False
        if tie:
            game_over = True
            winner = 0

def game_result(winner):
    global game_over
    if winner != 0:
        result = "Player " + str(winner) + " won!!"
    elif winner == 0:
        result = "You guys tied!"

    end_text = FONT.render(result, True, BLACK)
    p.draw.rect(WINDOW, GREY, (WIDTH // 2 - 100, HEIGHT // 2 - 60, 200, 50))
    WINDOW.blit(end_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))

    play_again = "Play Again?"
    again_text = FONT.render(play_again, True, BLACK)
    p.draw.rect(WINDOW, GREY, replay_box)
    WINDOW.blit(again_text, (WIDTH // 2 - 80, HEIGHT // 2 + 10))


def main():
    global clicked, player, pos, location, game_over, winner
    run = True
    while run:


        draw_grid()
        draw_location()
        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            if game_over == False:
                if event.type == p.MOUSEBUTTONDOWN and not clicked:
                    clicked = True
                if event.type == p.MOUSEBUTTONUP and clicked:
                    clicked = False
                    pos = p.mouse.get_pos()
                    tile_x = pos[0] // 100
                    tile_y = pos[1] // 100
                    if location[tile_x][tile_y] == 0:
                        location[tile_x][tile_y] = player
                        player *= -1
                        check_game_over()

        if game_over:
            game_result(winner)
            if event.type == p.MOUSEBUTTONDOWN and not clicked:
                clicked = True
            if event.type == p.MOUSEBUTTONUP and clicked:
                clicked = False
                pos = p.mouse.get_pos()
                if replay_box.collidepoint(pos):
                    game_over = False
                    player = 1
                    pos = (0,0)
                    location = []
                    winner = 0
                    for x in range (3):
                        row = [0] * 3
                        location.append(row)

        p.display.update()
    p.quit()

if __name__ == "__main__":
    main()
