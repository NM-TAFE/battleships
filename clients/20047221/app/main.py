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

global numA

numB = 1
numS = 3
numC = 1
numD = 2
numP = 2

while True:
    print('You have 1 A)ircraft Carrier, 1 B)attleship, 3 S)ubmarines, 1 C)ruiser, 2 D)estroyers, and 2 P)atrol Boats.')
    Ship = input('Choose a Ship to Place> ')
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

    print("""U)p, D)own, L)eft, or R)ight?""")
    Direction = input('Choose a Direction> ')
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
    s = input('Your move> ')
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
    print('You hit the target!')
    enemyGrid[current_y][current_x] = 'X'


@battleship.on()
def miss():
    print('Aww.. You missed!')
    enemyGrid[current_y][current_x] = 'O'


@battleship.on()
def win():
    print('Yay! You won!')
    enemyGrid[current_y][current_x] = 'X'
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
        print("""H)it, M)iss, or D)efeat?""")
        s = input('Enter status> ')
        _s = s[0].upper()
        if _s == 'H':
            playerGrid[enemy_y][enemy_x] = 'X'
            battleship.hit()
            break
        elif _s == 'M':
            playerGrid[enemy_y][enemy_x] = 'X'
            battleship.miss()
            break
        elif _s == 'D':
            playerGrid[enemy_y][enemy_x] = 'O'
            battleship.defeat()
            break
        else:
            continue


print('Waiting for the game to start...')
battleship.join()
while playing.is_set():
    time.sleep(1.0)
