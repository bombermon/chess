class Chess_figure(object):

    def __init__(self, Table, pos_y, pos_x, color):
        self.place = Table
        self.y = pos_x
        self.x = pos_y
        self.type = ''
        self.color = color
        self.symbol = ''

class King(Chess_figure):

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        self.type = "King"
        if self.color == "W":
            self.symbol = "♔"
        elif self.color == "B":
            self.symbol = "♚"


class Queen(Chess_figure):

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        self.type = "King"
        if self.color == "W":
            self.symbol = "♕"
        elif self.color == "B":
            self.symbol = "♛"


class Rook(Chess_figure):

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        self.type = "King"
        if self.color == "W":
            self.symbol = "♖"
        elif self.color == "B":
            self.symbol = "♜"


class Bishop(Chess_figure):

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        self.type = "King"
        if self.color == "W":
            self.symbol = "♗"
        elif self.color == "B":
            self.symbol = "♝"


class Knight(Chess_figure):

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        self.type = "King"
        if self.color == "W":
            self.symbol = "♘"
        elif self.color == "B":
            self.symbol = "♞"


class Pawn(Chess_figure):

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        self.type = "King"
        if self.color == "W":
            self.symbol = "♙"
        elif self.color == "B":
            self.symbol = "♟"


class Table(object):

    def __init__(self):
        self.matrix = [
    [Rook(self, 0, 0, "B"), Knight(self, 0, 1, "B"), Bishop(self, 0, 2,"B"), Queen(self, 0, 3,"B"), King(self, 0, 4,"B"), Bishop(self, 0, 5,"B"), Knight(self, 0, 6, "B"), Rook(self, 0, 7, "B")],
    [Pawn(self, 1, 0,"B"), Pawn(self, 1, 1,"B"), Pawn(self, 1, 2,"B"), Pawn(self, 1, 3,"B"), Pawn(self, 1, 4,"B"), Pawn(self, 1, 5,"B"), Pawn(self, 1, 6,"B"), Pawn(self, 1, 7,"B")],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None],
    [Pawn(self, 6, 0,"W"), Pawn(self, 6, 1,"W"), Pawn(self, 6, 2,"W"), Pawn(self, 6, 3,"W"), Pawn(self, 6, 4,"W"), Pawn(self, 6, 5,"W"), Pawn(self, 6, 6,"W"), Pawn(self, 6, 7,"W")],
    [Rook(self, 7, 0, "W"), Knight(self, 7, 1, "W"), Bishop(self, 7, 2,"W"), Queen(self, 7, 3,"W"), King(self, 7, 4,"W"), Bishop(self, 7, 5,"W"), Knight(self, 7, 6, "W"), Rook(self, 7, 7, "W")]]

    def print(self):
        print('  a b c d e f g h')
        for i in range(8):
            print("", i+1, end="")
            for j in range(8):
                if self.matrix[i][j] != None:
                    print(self.matrix[i][j].symbol, end=' ')
                elif (i + j) % 2 == 0:
                    print("⬜ ", end="")
                else:
                    print("⬛ ", end="")
            print()

class Game(object):

    def __init__(self):
        self.table = Table()
        self.turn = 1

game1 = Game()
game1.table.print()