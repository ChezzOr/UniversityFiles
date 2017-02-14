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

    # Check if the piece has made a movement (for special movement validation)
    def hasMoved(self):
        return self.moved()

    # Set the moved attribute to true to avoid special movements
    def setMoved(self):
        self.moved = True