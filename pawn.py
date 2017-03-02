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

    # Check if the piece has made a movement (for special movement validation)
    def hasMoved(self):
        return self.moved()

    # Set the moved attribute to true to avoid special movements
    def setMoved(self):
        self.moved = True

    def get_fpw(self):
        return "sprites/pw.png"

    def get_fpb(self):
        return "sprites/pb.png"