# Вверх
        for i in range(x - 1, -1, -1):
            if self.table.matrix[i][y] is None:
                self.matrix[i][y].matrix = '*'
            elif self.table.matrix[i][y] is not None:
                if black.match(self.table.matrix[i][y]) != None:
                    self.table.matrix[i][y] = 'X'
                    break
                else:
                    break

        # Влево
        for i in range(y - 1, -1, -1):
            if self.table.matrix[x][i] == '.':
                self.table.matrix[x][i] = '*'
            elif self.table.matrix[x][i] != '.':
                if black.match(self.table.matrix[i][y]) != None:
                    self.table.matrix[x][i] = 'X'
                    break
                else:
                    break

        # Вправо
        for i in range(y + 1, 8):
            if self.table.matrix[x][i] == '.':
                self.table.matrix[x][i] = '*'
            elif self.table.matrix[x][i] != '.':
                if black.match(self.table.matrix[x][i]) != None:
                    self.table.matrix[x][i] = 'X'
                    break
                else:
                    break
        # Вверх вправо
        for i in range(x - 1, -1, -1):
            if self.table.matrix[i][y + (x - i)] == '.' and (0 <= y + (x - i) <= 7):
                self.table.matrix[i][y + (x - i)] = '*'
            elif self.table.matrix[i][y + (x - i)] != '.':
                if (0 <= y + (x - i) <= 7) and black.match(self.table.matrix[i][y + (x - i)]) != None:
                    self.table.matrix[i][y + (x - i)] = 'X'
                    break
                else:
                    break
        # Вверх влево
        for i in range(x - 1, -1, -1):
            if self.table.matrix[i][y - (x - i)] == '.' and (0 <= y - (x - i) <= 7):
                self.table.matrix[i][y - (x - i)] = '*'
            elif self.table.matrix[i][y - (x - i)] != '.':
                if (0 <= y - (x - i) <= 7) and black.match(self.table.matrix[i][y - (x - i)]) != None:
                    self.table.matrix[i][y - (x - i)] = 'X'
                    break
                else:
                    break

        # Вниз
        # Вниз
        for i in range(x + 1, 8):
            if self.table.matrix[i][y] == '.':
                self.table.matrix[i][y] = '*'
            elif matrixp[i][y] != '.':
                if white.match(self.table.matrix[i][y]) != None:
                    self.table.matrix[i][y] = 'X'
                    break
                else:
                    break

        # Влево
        for i in range(y - 1, -1, -1):
            if self.table.matrix[x][i] == '.':
                self.table.matrix[x][i] = '*'
            elif self.table.matrix[x][i] != '.':
                if white.match(self.table.matrix[x][i]) != None:
                    self.table.matrix[x][i] = 'X'
                    break
                else:
                    break

                # Вправо
        for i in range(y + 1, 8):
            if self.table.matrix[x][i] == '.':
                self.table.matrix[x][i] = '*'
            elif self.table.matrix[x][i] != '.':
                if white.match(self.table.matrix[x][i]) != None:
                    self.table.matrix[x][i] = 'X'
                    break
                else:
                    break
        # Вниз вправо
        for i in range(x + 1, 8):
            if self.table.matrix[i][y + (i - x)] == '.' and (0 <= y + (i - x) <= 7):
                self.table.matrix[i][y + (i - x)] = '*'
            elif self.table.matrix[i][y + (i - x)] != '.':
                if (0 <= y + (i - x) <= 7) and white.match(self.table.matrix[i][y + (i - x)]) != None:
                    self.table.matrix[i][y + (i - x)] = 'X'
                    break
                else:
                    break
        # Вниз влево
        for i in range(x + 1, 8):
            if self.table.matrix[i][y - (i - x)] == '.' and (0 <= y - (i - x) <= 7):
                self.table.matrix[i][y - (i - x)] = '*'
            elif self.table.matrix[i][y - (i - x)] != '.':
                if (0 <= y - (i - x) <= 7) and white.match(self.table.matrix[i][y - (i - x)]) != None:
                    self.table.matrix[i][y - (i - x)] = 'X'
                    break
                else:
                    break
        return 1