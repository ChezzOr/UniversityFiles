"""
Notation chess v1
Developed by Christopher Ojeda Rivera A01203980
"""

"""
Importing libraries and classes
"""
import pygame
from pygame import *
import tile, pawn, bishop, king, queen, knight, rook
import sys, os

"""
Function to load the tiles and form the board
The board is made from 64 tiles, with alternating colors
"""


def load():
    for x in range(0, 8):
        for y in range(0, 8):
            #Set individual tile information
            aux = tile.tile()
            if (x+y) % 2 != 0:
                aux.set_color(2)
            if y < 2 or 6 <= y:
                aux.set_occupied(True)
            aux.set_x(x+1)
            aux.set_y(y+1)
            aux.set_xpos(x * 60)
            aux.set_ypos(y * 60)
            board.append(aux)
    return

"""Function to load pieces on the board"""


def load_pieces():
    for x in pieces:
        #Load pawns
        if x == "p":
            for y in range(0,8):
                aux = pawn.pawn()
                aux.set_x(2)
                aux.set_y(y+1)
                white_pieces.append(aux)
                aux = pawn.pawn()
                aux.set_x(7)
                aux.set_y(8-y)
                aux.set_color(2)
                black_pieces.append(aux)
        #Load bishops
        if x == "b":
            for y in range(0,2):
                aux = bishop.bishop()
                aux.set_x(1)
                aux.set_y(3+y*3)
                white_pieces.append(aux)
                aux = bishop.bishop()
                aux.set_x(8)
                aux.set_y(3 + y * 3)
                aux.set_color(2)
                black_pieces.append(aux)
        #Load knights
        if x == "n":
            for y in range(0,2):
                aux = knight.knight()
                aux.set_x(1)
                aux.set_y(2 + y * 5)
                white_pieces.append(aux)
                aux = knight.knight()
                aux.set_x(8)
                aux.set_y(2 + y * 5)
                aux.set_color(2)
                black_pieces.append(aux)
        #Load rooks
        if x == "r":
            for y in range(0,2):
                aux = rook.rook()
                aux.set_x(1)
                aux.set_y(1 + y * 7)
                white_pieces.append(aux)
                aux = rook.rook()
                aux.set_x(8)
                aux.set_y(1 + y * 7)
                aux.set_color(2)
                black_pieces.append(aux)
        #Load queens
        if x == "q":
            aux = queen.queen()
            aux.set_x(1)
            aux.set_y(5)
            white_pieces.append(aux)
            aux = queen.queen()
            aux.set_x(8)
            aux.set_y(5)
            aux.set_color(2)
            black_pieces.append(aux)
        #Load kings
        if x == "k":
            aux = king.king()
            aux.set_x(1)
            aux.set_y(4)
            white_pieces.append(aux)
            aux = king.king()
            aux.set_x(8)
            aux.set_y(4)
            aux.set_color(2)
            black_pieces.append(aux)

"""Function to draw the pieces on the board"""


def draw_pieces(screen, board):
    for x in white_pieces:
        img = image.load(x.get_fpw()).convert_alpha()
        screen.blit(img, (board[(x.get_x()-1)+(x.get_y()-1)*8].get_xpos()+50, board[(x.get_x()-1)+(x.get_y()-1)*8].get_ypos()+100))

    for y in black_pieces:
        img = image.load(y.get_fpb()).convert_alpha()
        screen.blit(img, (board[(y.get_x()-1)+(y.get_y()-1)*8].get_xpos()+50, board[(y.get_x()-1)+(y.get_y()-1)*8].get_ypos()+100))

"""
Function to draw the input box an the box containing the previous movements
"""


def draw_input_box(screen, turn):
    # Remaining space 900 - 580, 320, top 620 120
    pygame.draw.rect(screen, white, (600, 60, 280, 470))
    pygame.draw.rect(screen, black, (600, 60, 280, 470), 1)
    pygame.draw.rect(screen, white, (600, 530, 280, 30))
    pygame.draw.rect(screen, black, (600, 530, 280, 30), 1)
    if turn == 1:
        label = registryFont.render(box_message[0], 1, black)
    else:
        label = registryFont.render(box_message[1], 1, black)
    screen.blit(label, (610, 540))


"""
Functions to obtain the user input and display it to screen
"""


# Method from code inputbox.py, more information at: http://www.pygame.org/pcr/inputbox/
# The method obtains the keydown event to obtain the pressed key
def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            #print(str(event.key))
            return event.key
        elif event.type == QUIT:
            exit(0)
        else:
            pass


def get_user_input(screen):
    user_input = ''
    while 1:
        pressed_key = get_key()
        if pressed_key == K_BACKSPACE:
            user_input = user_input[:-1]
        elif pressed_key == K_RETURN:
            break
        elif pressed_key in possible_keys:
            user_input += str(chr(pressed_key))
        #print(user_input)
        pygame.draw.rect(screen, white, (720, 540, 60, 19))
        label = registryFont.render(user_input, 1, black)
        screen.blit(label, (720, 540))
        pygame.display.flip()
    return user_input


"""
Function to process and validate user input
"""


def validate_input(input_string, turn):
    print(input_string)
    if len(input_string) < 3:
        return False
    if 'x' in input_string and len(input_string) < 6:
        return False
    if input_string in special_moves:
        return True
    elif input_string[0] in pieces:
        if turn == 1:
            possible_piece = [piece for piece in white_pieces
                              if piece.get_name() == input_string[0]
                              and piece.validate_move(input_string)]
        else:
            possible_piece = [piece for piece in black_pieces
                              if piece.get_name() == input_string[0]
                              and piece.validate_move(input_string)]
        print(possible_piece)
        if len(possible_piece) == 0:
            return False
        if 'x' in input_string:
            print(board[8*int(input_string[5])+ord(input_string[4]) - 97].get_occupied())
            print(8*(int(input_string[5])-1)+ord(input_string[4]) - 97)
            if board[8*int(input_string[5])+ord(input_string[4]) - 97].get_occupied():
                remove_piece(input_string)
                board[8*int(input_string[5])+ord(input_string[4]) - 97].set_occupied(False)
                possible_piece[0].move(input_string)
                return True
            else:
                return False
        else:
            if not board[8*int(input_string[2])+ord(input_string[1]) - 97].get_occupied():
                board[8 * int(input_string[2]) + ord(input_string[1]) - 97].set_occupied(True)
                possible_piece[0].move(input_string)
                return True
            else:
                return False
    else:
        return False


'''
Remove piece if taken
'''


def remove_piece(input_string):
    [black_pieces.pop(idx) for idx, piece in enumerate(black_pieces)
     if piece.get_x() == int(input_string[5])
     and piece.get_y() == (ord(input_string[4]) - 96)]


"""
Define the global variables
"""
# Init the pygame library
pygame.init()

# Array containing the pieces
pieces = ["p", "b", "n", "r", "q", "k"]
white_pieces = []
black_pieces = []

# Letters of the board
letters = 'ABCDEFGH'

# Initiate the board array which will store the tiles for drawing the board
board = []

# Define game colors
white = (255, 255, 255)
black = (47, 79, 79)
background = (255, 204, 153)
background_board = (220,220,220)

# Set font for board
boardFont = pygame.font.SysFont("monospace", 25)

# Set font for movement
registryFont = pygame.font.SysFont("monospace", 14)

# Array for board coordinates
boardcoord = []

# Array for input box
box_message = ['White\'s move: ', 'Black\'s move: ']

# Array for possible inputs
possible_keys = [K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_o, K_k, K_q,
                 K_b, K_n, K_r, K_e, K_p, K_x, K_a, K_c, K_d, K_e, K_f,
                 K_g, K_h, K_MINUS, K_PLUS]

# Array for possible special movements
special_moves = ['o-o-o', 'o-o']

"""
Main function of the game
This function handles the processing of data
Also it handles the GUI and the multiple events of the game
"""


def main():
    # Load the board
    load()
    # Set the board coordinates
    boardcoord.append(board[0].get_xpos()+20)
    boardcoord.append(board[0].get_ypos()+120)
    # Set the turn
    turn = 1
    # Set the flag for mistake in movement
    no_valid_move = 0
    # Initiate the run status
    run = True
    # Cicle to process the information and the GUI
    load_pieces()
    # Setting screen size
    screen = pygame.display.set_mode((900, 620))
    while (run):
        # Adding background
        screen.fill(background)
        # Drawing the background for the board space
        pygame.draw.rect(screen, background_board, (0, 0, 580, 620), 0)
        # Window controls
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
        # Drawing the board through tiles
        for x in board:
            # Alternating colors
            if x.get_color() % 2 == 0:
                color = black
            else:
                color = white
            # Drawing a single tile
            pygame.draw.rect(screen, color, (x.get_xpos()+50, x.get_ypos()+100, 60, 60), 0)
        # Drawing board coordinates
        for x in range(0,8):
            # X ayis
            label = boardFont.render(str(x+1), 1,black)
            screen.blit(label, (boardcoord[0]+10, boardcoord[1]+(x*60)))
            # Y axis
            label = boardFont.render(letters[x], 1, black)
            screen.blit(label, (boardcoord[0]+(x*60)+50, boardcoord[1] + 460))
        # Loading and drawing pieces on screen
        draw_pieces(screen, board)

        # Drawing the input box
        draw_input_box(screen, turn)
        pygame.display.flip()

        # Print a message if the previous movement was not valid
        if no_valid_move != 0:
            pygame.draw.rect(screen, white, (715, 560, 165, 19))
            pygame.draw.rect(screen, black, (715, 560, 165, 19), 1)
            label = registryFont.render('Not a valid movement', 1, black)
            screen.blit(label, (717, 561))
            pygame.display.flip()

        # Process user input
        if validate_input(get_user_input(screen), turn):
            pygame.draw.rect(screen, background, (720, 561, 60, 19))
            turn = -turn
            no_valid_move = 0
        else:
            pygame.draw.rect(screen, background, (720, 561, 60, 19))
            no_valid_move = 1

    # Exit application
    pygame.quit()

#Defining the default method for execution
if __name__ == "__main__":
    main()