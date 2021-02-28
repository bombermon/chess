a = [["*", "*", "*", "*", "*", "*"],
     ["*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*"],
     ["*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*"]]


def printmatrix(a):
    print('  0 1 2 3 4 5')
    for i in range(6):
        print(i, end=' ')

        for j in range(6):
            print(a[i][j], end=' ')
        print()


a[2][2] = 'П'
printmatrix(a)
x_start, y_start = (int(i) for i in input().split())

x_stop = 1
y_stop = 1
state = 0

if (abs(x_start - x_stop) == abs(y_start - y_stop)):
    a[x_stop][y_stop] = 'E'
    a[x_start][y_start] = 'S'
    state = 'diagonal'

    temp_start_x, temp_stop_x = x_start, x_stop
    temp_start_y, temp_stop_y = y_start, y_stop

    if (temp_start_x < temp_stop_x) and (temp_start_y < temp_stop_y):
        for i in range(temp_start_x + 1, temp_stop_x):
            temp_start_y += 1
            a[i][temp_start_y] = 'Z'

    elif temp_start_y > temp_stop_y and temp_start_x > temp_stop_x:
        buf1 = temp_start_x
        buf2 = temp_start_y
        temp_start_y, temp_start_x = temp_stop_y, temp_stop_x
        temp_stop_y, temp_stop_x = buf2, buf1
        for i in range(temp_start_x + 1, temp_stop_x):
            temp_start_y += 1
            a[i][temp_start_y] = 'Z'

    elif temp_start_y < temp_stop_y and temp_start_x > temp_stop_x:
        for i in range(temp_stop_y - 1, temp_start_y, -1):
            temp_stop_x += 1
            a[temp_stop_x][i] = 'Z'
            printmatrix(a)
    elif temp_stop_x > temp_start_x and temp_start_y > temp_stop_y:
        buf1 = temp_start_x
        buf2 = temp_start_y
        temp_start_x, temp_start_y = temp_stop_x, temp_stop_y
        temp_stop_x, temp_stop_y = buf1, buf2
        for i in range(temp_stop_y - 1, temp_start_y, -1):
            temp_stop_x += 1
            a[temp_stop_x][i] = 'Z'
            printmatrix(a)








elif x_start == x_stop and y_start != y_stop:
    a[x_stop][y_stop] = 'E'
    a[x_start][y_start] = 'S'
    if y_start > y_stop:
        y_start, y_stop = y_stop, y_start
    for i in range(y_start + 1, y_stop):
        a[x_start][i] = 'Z'

    state = 'horizontal'
elif x_start != x_stop and y_start == y_stop:
    a[x_stop][y_stop] = 'E'
    a[x_start][y_start] = 'S'
    if x_start > x_stop:
        x_start, x_stop = x_stop, x_start
    for i in range(x_start + 1, x_stop):
        a[i][y_start] = 'Z'
    state = 'vertical'
else:
    print('Сюда нельзя')
printmatrix(a)
print(state)
