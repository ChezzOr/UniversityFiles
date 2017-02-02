import pygame
from pygame import *
import tile

def load():
    for x  in range(0,7):
        for y in range(0,7):
            aux = tile.tile()
            if (x+y)%2!=0:
                aux.set_color(2)
            aux.set_x(x+1)
            aux.set_y(y+1)
            aux.set_xpos(x * 60)
            aux.set_ypos(y * 60)
            board.append(aux)
    return

pygame.init()
pieces = ["p","b","n","r","q","k"]
letters = "ABCDEFGH"
board = []
white = (255,255,255)
black = (0,0,0)
background = (255,204,153)
background_board = (137, 68, 21)
myfont = pygame.font.SysFont("monospace", 25)
boardcoord = []
def main():
    load()
    boardcoord.append(board[0].get_xpos()+20);
    boardcoord.append(board[0].get_ypos()+120);
    run = True
    while (run):
        screen = pygame.display.set_mode((800, 560))
        screen.fill(background)
        pygame.draw.rect(screen, background_board,(0,0,540,560),0)
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
        for x in board:
            if x.get_color() % 2 == 0:
                color = black
            else:
                color = white
            pygame.draw.rect(screen, color, (x.get_xpos()+50, x.get_ypos()+100, 60, 60), 0)
        for x in range(0,7):
            label = myfont.render(str(x+1), 1,black)
            screen.blit(label,(boardcoord[0],boardcoord[1]+(x*60)))
            label = myfont.render(letters[x], 1, black)
            screen.blit(label,(boardcoord[0]+(x*60)+50, boardcoord[1] + 400))
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()