board = {0: ' ', 1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' '}
coordinates = [['1', '3'], ['2', '3'], ['3', '3'],
               ['1', '2'], ['2', '2'], ['3', '2'],
               ['1', '1'], ['2', '1'], ['3', '1']]


def printed():
    print('''---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------'''.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))


printed()
turn = 'X'
n = 1
while n < 10:
    move = input('Enter the coordinates: ').split()
    if not move[0].isdecimal() and not move[1].isdecimal():
        print('You should enter numbers!')
        continue
    elif move not in coordinates:
        print('Coordinates should be from 1 to 3!')
        continue
    else:
        for number, coordinate in enumerate(coordinates):
            if move == coordinate:
                board[number] = turn
                coordinates.remove(coordinate)
                coordinates.insert(number, turn)

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        printed()
        n = n + 1
        for i in coordinates:
            if all(i) is 'X' or 'O':
                print('Draw')

        if 'X' == coordinates[0] == coordinates[1] == coordinates[2] or \
                'X' == coordinates[3] == coordinates[4] == coordinates[5] or \
                'X' == coordinates[6] == coordinates[7] == coordinates[8] or \
                'X' == coordinates[0] == coordinates[3] == coordinates[6] or \
                'X' == coordinates[1] == coordinates[4] == coordinates[7] or \
                'X' == coordinates[2] == coordinates[5] == coordinates[8] or \
                'X' == coordinates[0] == coordinates[4] == coordinates[8] or \
                'X' == coordinates[2] == coordinates[4] == coordinates[6]:
            print('X wins')
            break
        elif 'O' == coordinates[0] == coordinates[1] == coordinates[2] or \
                'O' == coordinates[3] == coordinates[4] == coordinates[5] or \
                'O' == coordinates[6] == coordinates[7] == coordinates[8] or \
                'O' == coordinates[0] == coordinates[3] == coordinates[6] or \
                'O' == coordinates[1] == coordinates[4] == coordinates[7] or \
                'O' == coordinates[2] == coordinates[5] == coordinates[8] or \
                'O' == coordinates[0] == coordinates[4] == coordinates[8] or \
                'O' == coordinates[2] == coordinates[4] == coordinates[6]:
            print('O wins')
            break
