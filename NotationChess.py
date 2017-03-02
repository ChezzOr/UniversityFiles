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
                aux.set_y(y)
                white_pieces.append(aux)
                aux = pawn.pawn()
                aux.set_x(7)
                aux.set_y(7-y)
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
            aux.set_y(4)
            white_pieces.append(aux)
            aux = queen.queen()
            aux.set_x(8)
            aux.set_y(4)
            aux.set_color(2)
            black_pieces.append(aux)
        #Load kings
        if x == "k":
            aux = king.king()
            aux.set_x(1)
            aux.set_y(5)
            white_pieces.append(aux)
            aux = king.king()
            aux.set_x(8)
            aux.set_y(5)
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
Define the global variables
"""
# Init the pygame library
pygame.init()

# Array containing the pieces
pieces = ["p", "b", "n", "r", "q", "k"]
white_pieces = []
black_pieces = []

#Letters of the board
letters = "ABCDEFGH"

#Initiate the board array which will store the tiles for drawing the board
board = []

#Define game colors
white = (255, 255, 255)
black = (47, 79, 79)
background = (255, 204, 153)
background_board = (220,220,220)

#Set font
myfont = pygame.font.SysFont("monospace", 25)

#Array for board coordinates
boardcoord = []

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
    # Initiate the run status
    run = True
    # Cicle to process the information and the GUI
    while (run):
        # Setting screen size
        screen = pygame.display.set_mode((900, 620))
        # Adding background
        screen.fill(background)
        # Drawing the background for the board space
        pygame.draw.rect(screen, background_board,(0,0,580,620),0)
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
            label = myfont.render(str(x+1), 1,black)
            screen.blit(label,(boardcoord[0]+10,boardcoord[1]+(x*60)))
            # Y axis
            label = myfont.render(letters[x], 1, black)
            screen.blit(label,(boardcoord[0]+(x*60)+50, boardcoord[1] + 460))
        load_pieces()
        draw_pieces(screen, board)
        # Update screen to show changes
        # pygame.display.update()
        # time.wait(1)
        pygame.display.flip()
    # Exit application
    pygame.quit()

#Defining the default method for execution
if __name__ == "__main__":
    main()