# PART ONE


def solution1():
    with open('dayfour.txt', 'r') as f:
        lines = f.read()
    lines.strip()

    lines = lines.splitlines()

    return xMasCounter(lines)

def xMasCounter(input):
    count = 0

    for r, row in enumerate(input):
        for c, char  in enumerate(input[r]):
            if char == 'X':
                numOfXmas = (up(input, r, c) + upRight(input, r, c) + right(input, r, c) + downRight(input, r, c) + down(input, r, c) + downLeft(input, r, c) + left(input, r, c) + leftUp(input, r, c))
                count += numOfXmas
            else:
                continue
    
    return count


def up(input, row, column):
    if row - 3 >= 0:
        if ((input[row-1][column] == 'M') and (input[row-2][column] == 'A') and (input[row-3][column] == 'S')):
            # print('up')
            return 1
            
        else:
            return 0
    else:
        return 0

def upRight(input, row, column):
    if (row - 3 >= 0) and (column + 3 < len(input[row])):
        if ((input[row-1][column+1] == 'M') and (input[row-2][column+2] == 'A') and (input[row-3][column+3] == 'S')):
            # print('upright')
            return 1
        else:
            return 0
    else:
        return 0

def right(input, row, column):
    if (column + 3 < len(input[row])):
        if ((input[row][column+1] == 'M') and (input[row][column+2] == 'A') and (input[row][column+3] == 'S')):
            # print('right')
            return 1
        else:
            return 0
    else:
        return 0

def downRight(input, row, column):
    if ((row + 3 < len(input)) and (column + 3 < len(input[row]))):
        if ((input[row+1][column+1] == 'M') and (input[row+2][column+2] == 'A') and (input[row+3][column+3] == 'S')):
            # print('down right')
            return 1
        else:
            return 0
    else:
        return 0

def down(input, row, column):
    if (row + 3 < len(input)):
        if ((input[row+1][column] == 'M') and (input[row+2][column] == 'A') and (input[row+3][column] == 'S')):
            # print('down')
            return 1
        else:
            return 0
    else:
        return 0

def downLeft(input, row, column):
    if ((row + 3 < len(input)) and (column - 3 >= 0)):
        if ((input[row+1][column-1] == 'M') and (input[row+2][column-2] == 'A') and (input[row+3][column-3] == 'S')):
            # print('down left')
            return 1
        else:
            return 0
    else:
        return 0

def left(input, row, column):
    if column - 3 >= 0:
        if ((input[row][column-1] == 'M') and (input[row][column-2] == 'A') and (input[row][column-3] == 'S')):
            return 1
        else:
            return 0
    else:
        return 0

def leftUp(input, row, column):
    if ((row - 3 >= 0) and (column - 3 >= 0)):
        if ((input[row-1][column-1] == 'M') and (input[row-2][column-2] == 'A') and (input[row-3][column-3] == 'S')):
            return 1
        else:
            return 0
    else:
        return 0

print(solution1())

def solution2():
    with open('dayfour.txt', 'r') as f:
        lines = f.read()
    lines.strip()

    lines = lines.splitlines()

    return x_MasCounter(lines)


def x_MasCounter(input):
    count = 0

    for r, row in enumerate(input):
        for c, char  in enumerate(input[r]):
            if char == 'A':
                if (masDR(input, r, c) + masDL(input, r, c) + masUR(input, r, c) + masUL(input, r, c)) == 2:
                    count += 1
            else:
                continue
    
    return count

def masDR(input, row, column):
    if ((1 <= row < len(input) - 1) and (1 <= column < len(input[row]) - 1)):
        if ((input[row-1][column-1] == 'M') and (input[row+1][column+1] == 'S')):
            # print('down right')
            return 1
        else:
            return 0
    else:
        return 0

def masDL(input, row, column):
    if ((1 <= row < len(input) - 1) and (1 <= column < len(input[row]) - 1)):
        if ((input[row-1][column+1] == 'M') and (input[row+1][column-1] == 'S')):
            # print('down right')
            return 1
        else:
            return 0
    else:
        return 0

def masUR(input, row, column):
    if ((1 <= row < len(input) - 1) and (1 <= column < len(input[row]) - 1)):
        if ((input[row+1][column-1] == 'M') and (input[row-1][column+1] == 'S')):
            # print('down right')
            return 1
        else:
            return 0
    else:
        return 0

def masUL(input, row, column):
    if ((1 <= row < len(input) - 1) and (1 <= column < len(input[row]) - 1)):
        if ((input[row+1][column+1] == 'M') and (input[row-1][column-1] == 'S')):
            # print('down right')
            return 1
        else:
            return 0
    else:
        return 0
    
print(solution2())

# Final time to complete both: 1:17:57
