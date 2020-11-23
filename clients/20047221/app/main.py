import os
import threading
import time
from client import Battleship

grpc_host = os.getenv('GRPC_HOST', 'localhost')
grpc_port = os.getenv('GRPC_PORT', '50051')

playing = threading.Event()
playing.set()

battleship = Battleship(grpc_host=grpc_host, grpc_port=grpc_port)

playerGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

"""
playerGrid = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
              ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
              ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
              ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
              ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
              ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
              ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
              ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
              ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
              ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
"""

enemyGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

global current_x
global current_y

global fir_x
global fir_y

global sec_x
global sec_y

global thi_x
global thi_y

global fou_x
global fou_y

global fif_x
global fif_y

numA = 1
numB = 1
numS = 3
numC = 1
numD = 2
numP = 2

shipBlocks = 27

while True:
    if numA == 0 and numB == 0 and numS == 0 and numC == 0 and numD == 0 and numP == 0:
        print('All Ships have been Placed. Are you Happy with your Placement?')
        ready = input('Y / N > ')
        _ready = ready[0].upper()
        if _ready == 'Y':
            break
        elif _ready == 'N':
            print('Ship Placement has been Reset.')
            playerGrid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            numA = 1
            numB = 1
            numS = 3
            numC = 1
            numD = 2
            numP = 2
            continue

    print(
        f'You have {numA} A)ircraft Carrier, {numB} B)attleship, {numS} S)ubmarines, {numC} C)ruiser, {numD} D)estroyers, and {numP} P)atrol Boats.')
    Ship = input('Choose a Ship to Place > ')
    _Ship = Ship[0].upper()

    print('Where do you want to place the Aircraft Carrier?')
    A = input('Choose a Coordinate> ')
    _A = A[0].upper()
    for ACChar in _A:
        if ACChar.isdigit():
            first_x = int(ACChar) - 1
        elif ACChar.isupper():
            first_y = ord(ACChar) - 65
        else:
            print('Invalid Character')

    print('U)p, D)own, L)eft, or R)ight?')
    Direction = input('Choose a Direction > ')
    _Direction = Direction[0].upper()
    if _Direction == 'U':
        sec_y = fir_y - 1
        thi_y = fir_y - 2
        fou_y = fir_y - 3
        fif_y = fir_y - 4

        if _Ship == 'A' and (fir_y < 0 or sec_y < 0 or thi_y < 0 or fou_y < 0 or fif_y < 0):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'A' and numA == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'A':
            playerGrid[fir_y][fir_x] = 'A'
            playerGrid[sec_y][sec_x] = 'A'
            playerGrid[thi_y][thi_x] = 'A'
            playerGrid[fou_y][fou_x] = 'A'
            playerGrid[fif_y][fif_x] = 'A'

            numA -= 1
            break

        elif _Ship == 'B' and (fir_y < 0 or sec_y < 0 or thi_y < 0 or fou_y < 0):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'B' and numB == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'B':
            playerGrid[fir_y][fir_x] = 'B'
            playerGrid[sec_y][sec_x] = 'B'
            playerGrid[thi_y][thi_x] = 'B'
            playerGrid[fou_y][fou_x] = 'B'

            numB -= 1
            break

        elif _Ship == 'S' and (fir_y < 0 or sec_y < 0 or thi_y < 0):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'S' and numS == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'S':
            playerGrid[fir_y][fir_x] = 'S'
            playerGrid[sec_y][sec_x] = 'S'
            playerGrid[thi_y][thi_x] = 'S'

            numS -= 1
            break

        elif _Ship == 'C' and (fir_y < 0 or sec_y < 0 or thi_y < 0):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'C' and numC == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'C':
            playerGrid[fir_y][fir_x] = 'C'
            playerGrid[sec_y][sec_x] = 'C'
            playerGrid[thi_y][thi_x] = 'C'

            numC -= 1
            break

        elif _Ship == 'D' and (fir_y < 0 or sec_y < 0):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'D' and numD == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'D':
            playerGrid[fir_y][fir_x] = 'D'
            playerGrid[sec_y][sec_x] = 'D'

            numD -= 1
            break

        elif _Ship == 'P' and fir_y < 0:
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'P' and numP == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'P':
            playerGrid[fir_y][fir_x] = 'P'

            numP -= 1
            break

    elif _Direction == 'D':
        sec_y = fir_y + 1
        thi_y = fir_y + 2
        fou_y = fir_y + 3
        fif_y = fir_y + 4

        if _Ship == 'A' and (fir_y > 9 or sec_y > 9 or thi_y > 9 or fou_y > 9 or fif_y > 9):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'A' and numA == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'A':
            playerGrid[fir_y][fir_x] = 'A'
            playerGrid[sec_y][sec_x] = 'A'
            playerGrid[thi_y][thi_x] = 'A'
            playerGrid[fou_y][fou_x] = 'A'
            playerGrid[fif_y][fif_x] = 'A'

            numA -= 1
            break

        elif _Ship == 'B' and (fir_y > 9 or sec_y > 9 or thi_y > 9 or fou_y > 9):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'B' and numB == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'B':
            playerGrid[fir_y][fir_x] = 'B'
            playerGrid[sec_y][sec_x] = 'B'
            playerGrid[thi_y][thi_x] = 'B'
            playerGrid[fou_y][fou_x] = 'B'

            numB -= 1
            break

        elif _Ship == 'S' and (fir_y > 9 or sec_y > 9 or thi_y > 9):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'S' and numS == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'S':
            playerGrid[fir_y][fir_x] = 'S'
            playerGrid[sec_y][sec_x] = 'S'
            playerGrid[thi_y][thi_x] = 'S'

            numS -= 1
            break

        elif _Ship == 'C' and (fir_y > 9 or sec_y > 9 or thi_y > 9):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'C' and numC == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'C':
            playerGrid[fir_y][fir_x] = 'C'
            playerGrid[sec_y][sec_x] = 'C'
            playerGrid[thi_y][thi_x] = 'C'

            numC -= 1
            break

        elif _Ship == 'D' and (fir_y > 9 or sec_y > 9):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'D' and numD == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'D':
            playerGrid[fir_y][fir_x] = 'D'
            playerGrid[sec_y][sec_x] = 'D'

            numD -= 1
            break

        elif _Ship == 'P' and fir_y > 9:
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'P' and numP == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'P':
            playerGrid[fir_y][fir_x] = 'P'

            numP -= 1
            break

    elif _Direction == 'L':
        sec_x = fir_x - 1
        thi_x = fir_x - 2
        fou_x = fir_x - 3
        fif_x = fir_x - 4
        if _Ship == 'A' and (fir_x < 0 or sec_x < 0 or thi_x < 0 or fou_x < 0 or fif_x < 0):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'A' and numA == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'A':
            playerGrid[fir_y][fir_x] = 'A'
            playerGrid[sec_y][sec_x] = 'A'
            playerGrid[thi_y][thi_x] = 'A'
            playerGrid[fou_y][fou_x] = 'A'
            playerGrid[fif_y][fif_x] = 'A'

            numA -= 1
            break

        elif _Ship == 'B' and (fir_x < 0 or sec_x < 0 or thi_x < 0 or fou_x < 0):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'B' and numB == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'B':
            playerGrid[fir_y][fir_x] = 'B'
            playerGrid[sec_y][sec_x] = 'B'
            playerGrid[thi_y][thi_x] = 'B'
            playerGrid[fou_y][fou_x] = 'B'

            numB -= 1
            break

        elif _Ship == 'S' and (fir_x < 0 or sec_x < 0 or thi_x < 0):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'S' and numS == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'S':
            playerGrid[fir_y][fir_x] = 'S'
            playerGrid[sec_y][sec_x] = 'S'
            playerGrid[thi_y][thi_x] = 'S'

            numS -= 1
            break

        elif _Ship == 'C' and (fir_x < 0 or sec_x < 0 or thi_x < 0):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'C' and numC == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'C':
            playerGrid[fir_y][fir_x] = 'C'
            playerGrid[sec_y][sec_x] = 'C'
            playerGrid[thi_y][thi_x] = 'C'

            numC -= 1
            break

        elif _Ship == 'D' and (fir_x < 0 or sec_x < 0):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'D' and numD == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'D':
            playerGrid[fir_y][fir_x] = 'D'
            playerGrid[sec_y][sec_x] = 'D'

            numD -= 1
            break

        elif _Ship == 'P' and fir_x < 0:
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'P' and numP == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'P':
            playerGrid[fir_y][fir_x] = 'P'

            numP -= 1
            break

    elif _Direction == 'R':
        sec_x = fir_x + 1
        thi_x = fir_x + 2
        fou_x = fir_x + 3
        fif_x = fir_x + 4

        if _Ship == 'A' and (fir_x > 9 or sec_x > 9 or thi_x > 9 or fou_x > 9 or fif_x > 9):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'A' and numA == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'A':
            playerGrid[fir_y][fir_x] = 'A'
            playerGrid[sec_y][sec_x] = 'A'
            playerGrid[thi_y][thi_x] = 'A'
            playerGrid[fou_y][fou_x] = 'A'
            playerGrid[fif_y][fif_x] = 'A'

            numA -= 1
            break

        elif _Ship == 'B' and (fir_x > 9 or sec_x > 9 or thi_x > 9 or fou_x > 9):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'B' and numB == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'B':
            playerGrid[fir_y][fir_x] = 'B'
            playerGrid[sec_y][sec_x] = 'B'
            playerGrid[thi_y][thi_x] = 'B'
            playerGrid[fou_y][fou_x] = 'B'

            numB -= 1
            break

        elif _Ship == 'S' and (fir_x > 9 or sec_x > 9 or thi_x > 9):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'S' and numS == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'S':
            playerGrid[fir_y][fir_x] = 'S'
            playerGrid[sec_y][sec_x] = 'S'
            playerGrid[thi_y][thi_x] = 'S'

            numS -= 1
            break

        elif _Ship == 'C' and (fir_x > 9 or sec_x > 9 or thi_x > 9):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'C' and numC == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'C':
            playerGrid[fir_y][fir_x] = 'C'
            playerGrid[sec_y][sec_x] = 'C'
            playerGrid[thi_y][thi_x] = 'C'

            numC -= 1
            break

        elif _Ship == 'D' and (fir_x > 9 or sec_x > 9):
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'D' and numD == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'D':
            playerGrid[fir_y][fir_x] = 'D'
            playerGrid[sec_y][sec_x] = 'D'

            numD -= 1
            break

        elif _Ship == 'P' and fir_x > 9:
            print('Ship Goes Outside the Bounds of the Board.')
            continue

        elif _Ship == 'P' and numP == 0:
            print('No More Ships to Place.')
            continue

        elif _Ship == 'P':
            playerGrid[fir_y][fir_x] = 'P'

            numP -= 1
            break

    else:
        print('Invalid Direction.')
        continue


@battleship.on()
def begin():
    print('Game started!')


@battleship.on()
def start_turn():
    s = input('Your move > ')
    _s = s[0].upper()
    for char in s:
        if char.isdigit():
            global current_x
            current_x = int(char) - 1
        elif char.isupper():
            global current_y
            current_y = ord(char) - 65
        else:
            print('Invalid Character')

    battleship.attack(s)


@battleship.on()
def hit():
    enemyGrid[current_y][current_x] = 'X'
    print('You hit the target!')


@battleship.on()
def miss():
    enemyGrid[current_y][current_x] = 'O'
    print('Aww.. You missed!')


@battleship.on()
def win():
    enemyGrid[current_y][current_x] = 'X'
    print('Yay! You won!')
    playing.clear()


@battleship.on()
def lose():
    print('Aww... You lost...')
    playing.clear()


@battleship.on()
def attack(vector):
    vector = vector[0]
    print(f'Shot received at {vector}')
    enemy_x = 0
    enemy_y = 0
    _vector = vector[0].upper()
    for char in _vector:
        if char.isdigit():
            enemy_x = char - 1
        elif char.isupper():
            enemy_y = ord(char) - 65
        else:
            print('Invalid Character')

    while True:
        global shipBlocks

        if playerGrid[enemy_y][enemy_x] != 0:
            print(f'Enemy Hit a Ship at {vector}.')
            playerGrid[enemy_y][enemy_x] = 'X'
            shipBlocks -= 1
            if shipBlocks == 0:
                battleship.defeat()
            else:
                battleship.hit()
            break
        elif playerGrid[enemy_y][enemy_x] == 0:
            print(f'Enemy Missed at {vector}.')
            playerGrid[enemy_y][enemy_x] = 'O'
            battleship.miss()
            break
        else:
            continue


def show_player_grid():
    print('     1     2     3     4     5     6     7     8     9     10')
    z = 0
    while z < 10:
        a = playerGrid[z][0]
        b = playerGrid[z][0]
        c = playerGrid[z][0]
        d = playerGrid[z][0]
        e = playerGrid[z][0]
        f = playerGrid[z][0]
        g = playerGrid[z][0]
        h = playerGrid[z][0]
        i = playerGrid[z][0]
        j = playerGrid[z][0]
        Y = chr(z + 65)
        print('  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +')
        print(f'{Y} |  {a}  |  {b}  |  {c}  |  {d}  |  {e}  |  {f}  |  {g}  |  {h}  |  {i}  |  {j}  |')
        z += 1
    print('  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +')


def show_enemy_grid():
    print('     1     2     3     4     5     6     7     8     9     10')
    z = 0
    while z < 10:
        a = enemyGrid[z][0]
        b = enemyGrid[z][0]
        c = enemyGrid[z][0]
        d = enemyGrid[z][0]
        e = enemyGrid[z][0]
        f = enemyGrid[z][0]
        g = enemyGrid[z][0]
        h = enemyGrid[z][0]
        i = enemyGrid[z][0]
        j = enemyGrid[z][0]
        Y = chr(z + 65)
        print('  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +')
        print(f'{Y} |  {a}  |  {b}  |  {c}  |  {d}  |  {e}  |  {f}  |  {g}  |  {h}  |  {i}  |  {j}  |')
        z += 1
    print('  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +')


print('Waiting for the game to start...')
battleship.join()
while playing.is_set():
    time.sleep(1.0)

'''

     1     2     3     4     5     6     7     8     9     10
  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +
A |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +
B |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +
C |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +
D |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +
E |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +
F |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +
G |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +
H |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +
I |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +
J |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |  0  |
  + --- + --- + --- + --- + --- + --- + --- + --- + --- + --- +

'''