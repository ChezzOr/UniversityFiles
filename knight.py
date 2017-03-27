from piece import piece


class knight(piece):

    # Initiate instance
    def __init__(self):
        self.data = []
        self.name = 'n'

    """ Override of abstract class """

    # Method for recovering the movement of a piece
    # Return consists on an array of 3 numbers
    # Maximum quantity of square and possible axis, [4,8,3] 4 spaces in 8 possible directions identifies a knight, 3 means L movement
    def get_movement(self):
        return [4, 8, 3]

    def validate_move(self, movement):
        if 'x' in movement:
            y = ord(movement[4]) - 96
            x = int(movement[5])
        else:
            y = ord(movement[1]) - 96
            x = int(movement[2])

        if abs(self.x - x) == 2:
            if abs(self.y - y) == 1:
                return True
            else:
                return False
        elif abs(self.y - y) == 2:
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

    def get_fpw(self):
        return "sprites/nw.png"

    def get_fpb(self):
        return "sprites/nb.png"
