from piece import piece

class pawn(piece):
    """Attributes of the class"""
    moved = False

    # Initiate instance
    def __init__(self):
        self.data = []
        self.name = 'p'

    """ Override of abstract class """
    #Method for recovering the movement of a piece
    #Return consists on an array of 3 numbers
    #Maximum quantity of square and possible axis, [1,3,1] 8 spaces in 4 possible directions identifies a pawn, 1 means diagonal included
    def get_movement(self):
        if self.moved:
            return [1,3,1]
        else:
            return [2,1,0]

    def validate_move(self, movement):
        if 'x' in movement:
            #pe4xf5
            if self.x == int(movement[2]) and self.y == ord(movement[1]):
                y = ord(movement[4]) - 96
                x = int(movement[5])
                if abs(self.y - y) == 1:
                    if abs(self.x - x) == 1:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            y = ord(movement[1]) - 96
            x = int(movement[2])
            if abs(self.y - y) == 0:
                if self.moved is False:
                    if 0 < abs(self.x - x) <= 2:
                        return True
                    else:
                        return False
                else:
                    if abs(self.x - x) == 1:
                        return True
                    else:
                        return False
            else:
                return False

    def move(self, movement):
        if 'x' in movement:
            self.y = ord(movement[4]) - 96
            self.x = int(movement[5])
        else:
            self.y = ord(movement[1]) - 96
            self.x = int(movement[2])
        self.setMoved()


    # Check if the piece has made a movement (for special movement validation)
    def hasMoved(self):
        return self.moved

    # Set the moved attribute to true to avoid special movements
    def setMoved(self):
        self.moved = True

    def get_fpw(self):
        return "sprites/pw.png"

    def get_fpb(self):
        return "sprites/pb.png"
