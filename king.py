from piece import piece

class king(piece):
    """Attributes of the class"""
    moved = False

    # Initiate instance
    def __init__(self):
        self.data = []

    """ Override of abstract class """

    # Method for recovering the movement of a piece
    # Return consists on an array of 3 numbers
    # Maximum quantity of square and possible axis, [1,8,1] 1 space in 8 possible directions identifies a king, 1 means diagonal included
    def get_movement(self):
        return [1,8,1]

    def hasMoved(self):
        return self.moved()

    def setMoved(self):
        self.moved = True