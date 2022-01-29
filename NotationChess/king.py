from piece import piece

class king(piece):
    """Attributes of the class"""
    moved = False

    # Initiate instance
    def __init__(self):
        self.data = []
        self.name = 'k'

    """ Override of abstract class """

    # Method for recovering the movement of a piece
    # Return consists on an array of 3 numbers
    # Maximum quantity of square and possible axis, [1,8,1] 1 space in 8 possible directions identifies a king, 1 means diagonal included
    def get_movement(self):
        return [1,8,1]

    def validate_move(self, movement):
        if 'x' in movement:
            if self.x == int(movement[2]) and self.y == ord(movement[1]) - 96:
                y = ord(movement[4]) - 96
                x = int(movement[5])
                if abs(self.y - y) == abs(self.x - x) and abs(self.y - y) == 1:
                    return True
                elif abs(self.y - y) == 0 and abs(self.x - x) == 1:
                    return True
                elif abs(self.y - y) == 1 and abs(self.x - x) == 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            y = ord(movement[1]) - 96
            x = int(movement[2])
            if abs(self.y - y) == abs(self.x - x):
                return True
            elif abs(self.y - y) == 0 and abs(self.x - x) >= 1:
                return True
            elif abs(self.y - y) >= 1 and abs(self.x - x) == 0:
                return True
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
        return self.moved()

    # Set the moved attribute to true to avoid special movements
    def setMoved(self):
        self.moved = True

    def get_fpw(self):
        return "sprites/kw.png"

    def get_fpb(self):
        return "sprites/kb.png"