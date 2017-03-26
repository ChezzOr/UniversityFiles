"""Library for implementing abstract clases"""
from abc import ABCMeta, abstractmethod

class piece(metaclass=ABCMeta):
    #Defining class as abstract
    __metaclass__ = ABCMeta

    """Attributes of the class"""
    #Color of the piece 1 white, 2 black
    color = 1
    #Letters
    x = 1
    #Numbers
    y = 1
    #Alive indicator
    alive = True
    #Piece name
    name = ''
    # Conversion to letter
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    # Initiate instance
    def __init__(self):
        self.data = []

    """Getters and setters of the class"""

    def get_color(self):
        return self.color

    def set_color(self, col):
        self.color = col

    def get_x(self):
        return self.x

    def set_x(self, xn):
        self.x = xn

    def get_y(self):
        return self.y

    def set_y(self, yn):
        self.y = yn

    def isAlive(self):
        return self.alive

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    """Abstract methods"""
    @abstractmethod
    def get_movement(self):
        raise NotImplementedError()

    @abstractmethod
    def validate_move(self, movement):
        raise NotImplementedError()

    @abstractmethod
    def move(self, movement):
        raise NotImplementedError()