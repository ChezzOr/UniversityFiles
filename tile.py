class tile:
    color = 1
    '''Letters'''
    x = 1
    '''Numbers'''
    y = 1
    '''Coordinates'''
    xpos = 0
    ypos = 0
    '''Tile ocuppied'''
    occupied = False
    def __init__(self):
        self.data = []

    def get_color(self ):
        return self.color

    def set_color(self,col):
        self.color = col

    def get_x(self):
        return self.x

    def set_x(self,xn):
        self.x = xn

    def get_y(self):
        return self.y

    def set_y(self,yn):
        self.y = yn

    def get_xpos(self):
        return self.xpos

    def set_xpos(self,xn):
        self.xpos = xn

    def get_ypos(self):
        return self.ypos

    def set_ypos(self,yn):
        self.ypos = yn

    def get_occupied(self):
        return self.occupied

    def set_occupied(self,new):
        self.occupied = new