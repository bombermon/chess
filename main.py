"""
    Делаем задания номер:
        1) Фигуры
        2) Шашки
        5) Откаты СДЕЛАНО
        7) Подсказка хода  СДЕЛАНО
"""
import copy


class Chess_figure(object):

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

    def hint(self):
        x = self.x
        y = self.y
        matrix = [[None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None],
                  [None, None, None, None, None, None, None, None, None]]
        for i in range(8):
            for j in range(8):
                if self.table.matrix[y][x].move_able(j, i):
                    matrix[j][i] = '⭐'

        for i in range(8):
            for j in range(8):
                if matrix[j][i] != '⭐' and self.table.matrix[j][i] is not None:
                    matrix[j][i] = self.table.matrix[j][i].symbol
        print('ПОДСКАЗКА ДЛЯ ВАШЕГО ХОДА')
        print('  a  b  c d  e f g  h')
        for i in range(8):
            print("", i + 1, end="")
            for j in range(8):
                if matrix[i][j] is not None:
                    print(matrix[i][j], end=' ')
                elif (i + j) % 2 == 0:
                    print("⬜ ", end="")
                else:
                    print("⬛ ", end="")
            print()


class Queen(Chess_figure):

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        if self.color == "W":
            self.symbol = "♕"
        elif self.color == "B":
            self.symbol = "♛"

    def move_able(self, y, x):
        x_stop, y_stop = x, y
        y_start, x_start = self.y, self.x
        able = True
        if abs(x_start - x_stop) == abs(y_start - y_stop):

            temp_start_x, temp_stop_x = x_start, x_stop
            temp_start_y, temp_stop_y = y_start, y_stop

            if (temp_start_x < temp_stop_x) and (temp_start_y < temp_stop_y):
                for i in range(temp_start_x + 1, temp_stop_x):
                    temp_start_y += 1
                    if self.table.matrix[temp_start_y][i] is not None:
                        able = False


            elif temp_start_y > temp_stop_y and temp_start_x > temp_stop_x:
                buf1 = temp_start_x
                buf2 = temp_start_y
                temp_start_y, temp_start_x = temp_stop_y, temp_stop_x
                temp_stop_y, temp_stop_x = buf2, buf1
                for i in range(temp_start_x + 1, temp_stop_x):
                    temp_start_y += 1
                    if self.table.matrix[temp_start_y][i] is not None:
                        able = False


            elif temp_start_y < temp_stop_y and temp_start_x > temp_stop_x:
                for i in range(temp_stop_y - 1, temp_start_y, -1):
                    temp_stop_x += 1
                    if self.table.matrix[i][temp_stop_x] is not None:
                        able = False

            elif temp_stop_x > temp_start_x and temp_start_y > temp_stop_y:
                buf1 = temp_start_x
                buf2 = temp_start_y
                temp_start_x, temp_start_y = temp_stop_x, temp_stop_y
                temp_stop_x, temp_stop_y = buf1, buf2
                for i in range(temp_stop_y - 1, temp_start_y, -1):
                    temp_stop_x += 1
                    if self.table.matrix[i][temp_stop_x] is not None:
                        able = False

        elif x_start == x_stop and y_start != y_stop:
            if y_start > y_stop:
                y_start, y_stop = y_stop, y_start
            for i in range(y_start + 1, y_stop):
                if self.table.matrix[i][x_start] is not None:
                    able = False



        elif x_start != x_stop and y_start == y_stop:
            if x_start > x_stop:
                x_start, x_stop = x_stop, x_start
            for i in range(x_start + 1, x_stop):
                if self.table.matrix[y_start][i] is not None:
                    able = False



        else:
            able = False
            return able
        if self.table.matrix[y_stop][x_stop] is not None and self.table.matrix[y_start][x_start] is not None:
            if self.table.matrix[y_stop][x_stop].color == self.table.matrix[y_start][x_start].color:
                able = False
        return able


class King(Chess_figure):

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        if self.color == "W":
            self.symbol = "♔"
        elif self.color == "B":
            self.symbol = "♚"

    def move_able(self, y, x):
        x_stop, y_stop = x, y
        y_start, x_start = self.y, self.x

        if (x_start != x_stop or y_start != y_stop) and (abs(y_start - y_stop) < 2 and abs(x_start - x_stop)) < 2 and (
                self.table.matrix[y_stop][x_stop] is None or self.table.matrix[y_stop][x_stop].color != self.color):
            return True
        return False


class Rook(Chess_figure):

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        if self.color == "W":
            self.symbol = "♖"
        elif self.color == "B":
            self.symbol = "♜"

    def move_able(self, y, x):
        x_stop, y_stop = x, y
        y_start, x_start = self.y, self.x
        able = True

        if x_start == x_stop and y_start != y_stop:
            if y_start > y_stop:
                y_start, y_stop = y_stop, y_start
            for i in range(y_start + 1, y_stop):
                if self.table.matrix[i][x_start] is not None:
                    able = False



        elif x_start != x_stop and y_start == y_stop:
            if x_start > x_stop:
                x_start, x_stop = x_stop, x_start
            for i in range(x_start + 1, x_stop):
                if self.table.matrix[y_start][i] is not None:
                    able = False



        else:

            able = False
            return able
        if self.table.matrix[y_stop][x_stop] is not None and self.table.matrix[y_start][x_start] is not None:
            if self.table.matrix[y_stop][x_stop].color == self.table.matrix[y_start][x_start].color:
                able = False
        return able


class Bishop(Chess_figure):

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        if self.color == "W":
            self.symbol = "♗"
        elif self.color == "B":
            self.symbol = "♝"

    def move_able(self, y, x):
        x_stop, y_stop = x, y
        y_start, x_start = self.y, self.x
        able = True
        if abs(x_start - x_stop) == abs(y_start - y_stop):

            temp_start_x, temp_stop_x = x_start, x_stop
            temp_start_y, temp_stop_y = y_start, y_stop

            if (temp_start_x < temp_stop_x) and (temp_start_y < temp_stop_y):
                for i in range(temp_start_x + 1, temp_stop_x):
                    temp_start_y += 1
                    if self.table.matrix[temp_start_y][i] is not None:
                        able = False


            elif temp_start_y > temp_stop_y and temp_start_x > temp_stop_x:
                buf1 = temp_start_x
                buf2 = temp_start_y
                temp_start_y, temp_start_x = temp_stop_y, temp_stop_x
                temp_stop_y, temp_stop_x = buf2, buf1
                for i in range(temp_start_x + 1, temp_stop_x):
                    temp_start_y += 1
                    if self.table.matrix[temp_start_y][i] is not None:
                        able = False


            elif temp_start_y < temp_stop_y and temp_start_x > temp_stop_x:
                for i in range(temp_stop_y - 1, temp_start_y, -1):
                    temp_stop_x += 1
                    if self.table.matrix[i][temp_stop_x] is not None:
                        able = False

            elif temp_stop_x > temp_start_x and temp_start_y > temp_stop_y:
                buf1 = temp_start_x
                buf2 = temp_start_y
                temp_start_x, temp_start_y = temp_stop_x, temp_stop_y
                temp_stop_x, temp_stop_y = buf1, buf2
                for i in range(temp_stop_y - 1, temp_start_y, -1):
                    temp_stop_x += 1
                    if self.table.matrix[i][temp_stop_x] is not None:
                        able = False





        else:

            able = False
            return able
        if self.table.matrix[y_stop][x_stop] is not None and self.table.matrix[y_start][x_start] is not None:
            if self.table.matrix[y_stop][x_stop].color == self.table.matrix[y_start][x_start].color:
                able = False
        return able


class Knight(Chess_figure):

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        if self.color == "W":
            self.symbol = "♘"
        elif self.color == "B":
            self.symbol = "♞"

    def move_able(self, y, x):
        if 0 <= x <= 7 and 0 <= y <= 7:
            if (abs(self.y - y) == 2 and abs(self.x - x) == 1) or (abs(self.y - y) == 1 and abs(self.x - x) == 2):
                if self.table.matrix[y][x] is None or self.table.matrix[y][x].color != self.color:
                    return True
        return False


class Pawn(Chess_figure):

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        if self.color == "W":
            self.symbol = "♙"
        elif self.color == "B":
            self.symbol = "♟"

    def move_able(self, y, x):
        x_stop, y_stop = x, y
        x_start, y_start = self.x, self.y
        able = True

        if self.color == "W":
            if y_start == 6 and (y_start - y_stop) == 2 and x_start == x_stop:
                if self.table.matrix[y_stop][x_stop] is None and self.table.matrix[y_stop - 1][x_stop] is None:
                    return able
            elif (y_start - y_stop) == 1 and x_start == x_stop:
                if self.table.matrix[y_stop][x_stop] is None:
                    return able
            else:
                pass
                # Вверх вправо
            if (y_start - 1) == y_stop and (x_start + 1) == x_stop:
                if self.table.matrix[y_stop][x_stop] is not None:
                    if self.table.matrix[y_stop][x_stop].color != self.table.matrix[y_start][x_start].color:
                        return able

                # Вверх влево
            if (y_start - 1) == y_stop and (x_start - 1) == x_stop:
                if self.table.matrix[y_stop][x_stop] is not None:
                    if self.table.matrix[y_stop][x_stop].color != self.table.matrix[y_start][x_start].color:
                        return able

        elif self.color == "B":
            if y_start == 1 and (y_start - y_stop) == -2 and x_start == x_stop:
                if self.table.matrix[y_stop][x_stop] is None and self.table.matrix[y_stop + 1][x_stop] is None:
                    return able
            elif (y_start - y_stop) == -1 and x_start == x_stop:
                if self.table.matrix[y_stop][x_stop] is None:
                    return able
            else:
                pass

            # Вниз вправо
            if (y_start + 1) == y_stop and (x_start - 1) == x_stop:
                if self.table.matrix[y_stop][x_stop] is not None:
                    if self.table.matrix[y_stop][x_stop].color != self.table.matrix[y_start][x_start].color:
                        return able

                # Вниз влево
            if (y_start + 1) == y_stop and (x_start + 1) == x_stop:
                if self.table.matrix[y_stop][x_stop] is not None:
                    if self.table.matrix[y_stop][x_stop].color != self.table.matrix[y_start][x_start].color:
                        return able


class Dragon(Chess_figure):  # вперёд и по диагонали на 3 клетки

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        if self.color == "W":
            self.symbol = "D"
        elif self.color == "B":
            self.symbol = "d"

    def move_able(self, y, x):
        x_stop, y_stop = x, y
        x_start, y_start = self.x, self.y
        able = True

        if self.color == "W":
            if (y_start - y_stop) in [1, 2, 3] and x_start == x_stop:
                if self.table.matrix[y_stop][x_stop] is None:
                    return able
            else:
                pass
                # Вверх вправо
            if (y_start - 1) == y_stop and ((x_start - 1) == x_stop or (x_start + 1) == x_stop):
                if self.table.matrix[y_stop][x_stop] is None:
                    return able
            elif (y_start - 2) == y_stop and ((x_start - 2) == x_stop or (x_start + 2) == x_stop):
                if self.table.matrix[y_stop][x_stop] is None:
                    return able
            elif (y_start - 3) == y_stop and ((x_start - 3) == x_stop or (x_start + 3) == x_stop):
                if self.table.matrix[y_stop][x_stop] is None:
                    return able




        elif self.color == "B":

            if (y_start - y_stop) in [-1, -2, -3] and x_start == x_stop:
                if self.table.matrix[y_stop][x_stop] is None:
                    return able

            if (y_start + 1) == y_stop and ((x_start - 1) == x_stop or (x_start + 1) == x_stop):
                if self.table.matrix[y_stop][x_stop] is None:
                    return able
            elif (y_start + 2) == y_stop and ((x_start - 2) == x_stop or (x_start + 2) == x_stop):
                if self.table.matrix[y_stop][x_stop] is None:
                    return able
            elif (y_start + 3) == y_stop and ((x_start - 3) == x_stop or (x_start + 3) == x_stop):
                if self.table.matrix[y_stop][x_stop] is None:
                    return able


class Gnome(Chess_figure):  # вперёд и вправо на одну или две клетки

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        if self.color == "W":
            self.symbol = "G"
        elif self.color == "B":
            self.symbol = "g"

    def move_able(self, y, x):
        x_stop, y_stop = x, y
        x_start, y_start = self.x, self.y
        able = True

        if self.color == "W":
            if (x_start - x_stop) in [-1, -2] and y_start == y_stop:
                if self.table.matrix[y_stop][x_stop] is None:
                    return able
            elif (y_start - y_stop) in [1, 2] and x_start == x_stop:
                if self.table.matrix[y_stop][x_stop] is None:
                    return able


        elif self.color == "B":
            if (x_start - x_stop) in [1, 2] and y_start == y_stop:
                if self.table.matrix[y_stop][x_stop] is None:
                    return able
            elif (y_start - y_stop) in [-1, -2] and x_start == x_stop:
                if self.table.matrix[y_stop][x_stop] is None:
                    return able


class Mole(Chess_figure):  # пролезает везде в радиусе двух клеток

    def __init__(self, Table, pos_y, pos_x, color):
        super().__init__(Table, pos_y, pos_x, color)
        if self.color == "W":
            self.symbol = "M"
        elif self.color == "B":
            self.symbol = "m"

    def move_able(self, y, x):
        x_stop, y_stop = x, y
        x_start, y_start = self.x, self.y
        able = True

        if (x_start - x_stop) in [-1, -2, 1, 2] and y_start == y_stop:
            if self.table.matrix[y_stop][x_stop] is not None:
                if self.table.matrix[y_stop][x_stop].color and self.table.matrix[y_start][x_start].color:
                    able = False
                    return able
            return able
        elif (y_start - y_stop) in [-1, -2, 1, 2] and x_start == x_stop:
            if self.table.matrix[y_stop][x_stop] is not None:
                if self.table.matrix[y_stop][x_stop].color and self.table.matrix[y_start][x_start].color:
                    able = False
                    return able
            return able
            # Вверх вправо
        if ((y_start + 1) == y_stop or (y_start - 1) == y_stop) and (
                (x_start + 1) == x_stop or (x_start - 1) == x_stop):
            if self.table.matrix[y_stop][x_stop] is not None:
                if self.table.matrix[y_stop][x_stop].color and self.table.matrix[y_start][x_start].color:
                    able = False
                    return able
            return able
        elif ((y_start + 2) == y_stop or (y_start - 2) == y_stop) and (
                (x_start + 2) == x_stop or (x_start - 2) == x_stop):
            if self.table.matrix[y_stop][x_stop] is not None:
                if self.table.matrix[y_stop][x_stop].color and self.table.matrix[y_start][x_start].color:
                    able = False
                    return able
            return able


class Table(object):

    def __init__(self):
        self.matrix = [
            [Rook(self, 0, 0, "B"), Knight(self, 0, 1, "B"), Bishop(self, 0, 2, "B"), Queen(self, 0, 3, "B"),
             King(self, 0, 4, "B"), Bishop(self, 0, 5, "B"), Knight(self, 0, 6, "B"), Rook(self, 0, 7, "B")],
            [Pawn(self, 1, 0, "B"), Pawn(self, 1, 1, "B"), Dragon(self, 1, 2, "B"), Gnome(self, 1, 3, "B"),
             Mole(self, 1, 4, "B"), Pawn(self, 1, 5, "B"), Pawn(self, 1, 6, "B"), Pawn(self, 1, 7, "B")],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None],
            [Pawn(self, 6, 0, "W"), Pawn(self, 6, 1, "W"), Dragon(self, 6, 2, "W"), Gnome(self, 6, 3, "W"),
             Mole(self, 6, 4, "W"), Pawn(self, 6, 5, "W"), Pawn(self, 6, 6, "W"), Pawn(self, 6, 7, "W")],
            [Rook(self, 7, 0, "W"), Knight(self, 7, 1, "W"), Bishop(self, 7, 2, "W"), Queen(self, 7, 3, "W"),
             King(self, 7, 4, "W"), Bishop(self, 7, 5, "W"), Knight(self, 7, 6, "W"), Rook(self, 7, 7, "W")]]

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
        self.history = []
        self.current_color = None

    def cancel_move(self):
        if self.turn != 1:
            self.table = self.history.pop()
            self.turn -= 1

    def coord_input(self, place):
        let_2_dig = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        coord = input(f'Введите координату {place}: ').split()
        if len(coord) == 1 and coord[0] == "back":
            return -1, -1
        if len(coord) == 2:
            if let_2_dig.get(coord[0]) is not None:
                if coord[1].isdigit():
                    if 1 <= int(coord[1]) <= 8:
                        y, x = int(coord[1]) - 1, let_2_dig[coord[0]]
                        return y, x
        return False, False

    def current_color_check(self):
        print("Ходят ", end="")

        if self.turn % 2 == 1:
            print("белые!")
            self.current_color = 'W'
        else:
            self.current_color = 'B'
            print("черные!")

    def play(self):
        Is_Won = False
        while not Is_Won:
            turn_done = False
            while not turn_done:
                try:
                    game1.current_color_check()
                    game1.table.print()
                    y1, x1 = self.coord_input(place='фигуры')
                    if y1 == -1:
                        self.cancel_move()
                        turn_done = True
                        continue
                    if y1 is False:
                        print("Некорректный ввод, можно еще раз, только нормально, пожалуйста?")
                        continue
                    if self.table.matrix[y1][x1].color != self.current_color:
                        print('Не трогайте, пожалуйста, чужие фигуры!')
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
                        self.history.append(copy.deepcopy(self.table))
                        self.table.matrix[y1][x1].move(y2, x2)
                        turn_done = True
                        self.turn += 1
                    else:
                        print("Некорректный ввод, можно еще раз, только нормально, пожалуйста?")
                except:
                    print('Давайте по новой')


game1 = Game()
game1.play()
