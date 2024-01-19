import pygame
import sys
import time

pygame.init()

RESOLUTION = WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Tic Tac Toe in Python!")

big_font = pygame.font.Font('freesansbold.ttf', 85)

title_font = pygame.font.Font('freesansbold.ttf', 110)
option_font = pygame.font.Font('freesansbold.ttf', 80)

frame_rate = pygame.time.Clock()

# load in images
image_X = pygame.image.load('images/X.png')
image_X = pygame.transform.scale(image_X, (200, 200))

image_O = pygame.image.load('images/O.png')
image_O = pygame.transform.scale(image_O, (200, 200))

res_button = pygame.image.load('images/restart_button.png')
res_button = pygame.transform.scale(res_button, (400, 300))


def check_win_condition(board):
    for i in range(3):
        # rows
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != '':
            return True
        
        # columns
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != '':
            return True
    
    # diagonal L to R
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '':
        return True
    # diagonal R to L
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != '':
        return True
    
    return False

# effect when invalid spot is selected
def invalid_space():
    screen.fill((255, 0, 0)) # red
    pygame.display.flip()

    time.sleep(1)

# checks if spot is empty
def check_empty(board, x_coord, y_coord):
    return board[x_coord][y_coord] == ''


def draw_board(board, condition, curr_player):
    if condition == 0:
        # draws lines on board
        screen.fill((255, 255, 255)) # white

        for i in range(1,3):
            pygame.draw.line(screen, (0, 0, 0), (0, 200*i), (HEIGHT, 200*i), 5)
            pygame.draw.line(screen, (0, 0, 0), (200*i, 0), (200*i, WIDTH), 5)

        # draws current inputs onto board
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'X':
                    screen.blit(image_X, (200*i, 200*j))
                elif board[i][j] == 'O':
                    screen.blit(image_O, (200*i, 200*j))
                else: # nothing on board
                    pass
    elif condition == 1:
        screen.fill((0, 0, 0)) # black
        screen.blit(big_font.render(f"Player {curr_player} Won!", True, (255, 255, 255)), (5, 125))
        screen.blit(res_button, (100, 225))
    elif condition == 2:
        screen.fill((0, 0, 0))
        screen.blit(big_font.render(f"Game is Tied!", True, (255, 255, 255)), (5, 125))
        screen.blit(res_button, (100, 225))


def start_game():
    # Tic Tac Toe Game
    ROW = 3
    COL = 3
    board = [['' for j in range(COL)] for i in range(ROW)]

    players = ['X', 'O']
    num_turns = 0

    # 0 - continue game
    # 1 - Player X or O Won
    # 2 - Game Tied
    game_condition = 0

    while True:
        frame_rate.tick(60)
        
        draw_board(board, game_condition, players[num_turns%2-1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game_condition == 0: # mouse button and left click
                x_coord = event.pos[0] // 200
                y_coord = event.pos[1] // 200

                if check_empty(board, x_coord, y_coord):
                    board[x_coord][y_coord] = players[num_turns%2]
                    num_turns += 1

                    if num_turns >= 9: # tie
                        game_condition = 2
                    if check_win_condition(board):
                        game_condition = 1
                else:
                    invalid_space()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and game_condition != 0:
                board = [['' for j in range(COL)] for i in range(ROW)]
                num_turns = 0
                game_condition = 0
        
        pygame.display.flip()


def draw_intro():
    screen.fill((0, 0, 0))
    for i in range(4):
            pygame.draw.line(screen, (255, 255, 255), (0, 200*i), (HEIGHT, 200*i), 5)
            pygame.draw.line(screen, (255, 255, 255), (200*i, 0), (200*i, WIDTH), 5)

    screen.blit(title_font.render(f"Tic Tac Toe", True, (255, 255, 255), (0, 0, 0)), (5, 50))
    screen.blit(option_font.render(f"Play Game", True, (255, 255, 255), (0, 0, 0)), (110, 250))
    screen.blit(option_font.render(f"Quit", True, (255, 255, 255), (0, 0, 0)), (110, 390))


def intro():
    # introduction screen
    while True:
        frame_rate.tick(60)

        draw_intro()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x_coord = event.pos[0]
                y_coord = event.pos[1]
                
                print(event.pos)

                if (x_coord > 115 and y_coord > 254) and (x_coord < 523 and y_coord < 314): # play game
                    start_game()
                elif (x_coord > 110 and y_coord > 392) and (x_coord < 280 and y_coord < 457): # quit
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def main():
    intro()

if __name__ == '__main__':
    main()