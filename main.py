class Table(object):

    def __init__(self):
        self.matrix = []
        for i in range(8):
            self.matrix.append([None]*8)

class Chess_figure(object):

    def __init__(self, Table, pos_y, pos_x):
        self.place = Table
        self.y = pos_x
        self.x = pos_y
        self.type = ''
        self.color = ''


class

    if chosen_figure.cheek("e", 4):
        chosen_figure.move()
