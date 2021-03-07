"""
ШАШЕЧКИ
"""


class Checkers_figure(object):

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


class Checker(Checkers_figure):
    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        if self.color == "W":
            self.symbol = "⚪"
        elif self.color == "B":
            self.symbol = "⚫"


class Table(object):

    def __init__(self):
        self.matrix = [
            [None, Checker(self, 0, 1, "B"), None, Checker(self, 0, 3, "B"),
             None, Checker(self, 0, 5, "B"), None, Checker(self, 0, 7, "B")],
            [Checker(self, 1, 0, "B"), None, Checker(self, 1, 2, "B"), None,
             Checker(self, 1, 4, "B"), None, Checker(self, 1, 6, "B"), None],
            [None, Checker(self, 2, 1, "B"), None, Checker(self, 2, 3, "B"),
             None, Checker(self, 2, 5, "B"), None, Checker(self, 2, 7, "B")],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [Checker(self, 5, 0, "W"), None, Checker(self, 5, 2, "W"), None,
             Checker(self, 5, 4, "W"), None, Checker(self, 5, 6, "W"), None],
            [None, Checker(self, 6, 1, "W"), None, Checker(self, 6, 3, "W"),
             None, Checker(self, 6, 5, "W"), None, Checker(self, 6, 7, "W")],
            [Checker(self, 7, 0, "W"), None, Checker(self, 7, 2, "W"), None,
             Checker(self, 7, 4, "W"), None, Checker(self, 7, 6, "W"), None]]

    def print(self):
        print('  a  b  c d  e f g  h')
        for i in range(8):
            print("", i + 1, end="")
            for j in range(8):
                if self.matrix[i][j] is not None:
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

    def coord_input(self, place):
        let_2_dig = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        coord = input(f'Введите координату {place}: ').split()
        if len(coord) == 2:
            if let_2_dig.get(coord[0]) is not None:
                if coord[1].isdigit():
                    if 1 <= int(coord[1]) <= 8:
                        y, x = int(coord[1]) - 1, let_2_dig[coord[0]]
                        return y, x
        return False, False

    def play(self):
        Is_Won = False
        while not Is_Won:
            game1.table.print()
            turn_done = False
            print("Ходят ", end="")

            if self.turn % 2 == 1:
                print("белые")
            else:
                print("черные")

            while not turn_done:
                y1, x1 = self.coord_input(place='фигуры')
                if y1 is False:
                    print("Некорректный ввод, можно еще раз, только нормально, пожалуйста?")
                    continue
                self.table.matrix[y1][x1].hint()
                y2, x2 = self.coord_input(place='куда ходить')
                if y2 is False:
                    print("Некорректный ввод, можно еще раз, только нормально, пожалуйста?")
                    continue
                a = False
                if (self.table.matrix[y1][x1].color == "W" and self.turn % 2 == 1) or (
                        self.table.matrix[y1][x1].color == "B" and self.turn % 2 == 0):
                    print(self.table.matrix[y1][x1].symbol)
                    a = self.table.matrix[y1][x1].move_able(y2, x2)

                if a:
                    self.table.matrix[y1][x1].move(y2, x2)
                    turn_done = True
                else:
                    print("Некорректный ввод, можно еще раз, только нормально, пожалуйста?")
            self.turn += 1


game1 = Game()
game1.play()
