"""
ШАШЕЧКИ
"""


class checkers_figure(object):

    def __init__(self, Table, pos_y, pos_x, color):
        self.table = Table
        self.y = pos_y
        self.x = pos_x
        self.type = ''
        self.color = color
        self.symbol = ''

    def move(self, pos_y, pos_x):
        self.table.matrix[self.y][self.x] = None
        self.x = pos_x
        self.y = pos_y
        self.table.matrix[pos_y][pos_x] = self