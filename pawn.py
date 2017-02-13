from piece import piece

class pawn(piece):
    """Attributes of the class"""
    moved = False

    # Initiate instance
    def __init__(self):
        self.data = []

    """ Override of abstract class """
    #Method for recovering the movement of a piece
    #Return consists on an array of 3 numbers
    #Maximum quantity of square and possible axis, [1,3,1] 8 spaces in 4 possible directions identifies a pawn, 1 means diagonal included
    def get_movement(self):
        if self.moved:
            return [1,3,1]
        else:
            return [2,1,0]

    def hasMoved(self):
        return self.moved()

    def setMoved(self):
        self.moved = True
