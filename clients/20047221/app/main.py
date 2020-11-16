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

A = input('Where do you want to place the Aircraft Carrier? : ')
for Achar in A:
    if Achar.isdigit():
        x = int(Achar) - 1
    elif Achar.isupper():
        y = ord(Achar) - 65
    elif Achar.islower():
        y = ord(Achar) - 97
    else:
        print('Invalid Character')


@battleship.on()
def begin():
    print('Game started!')


@battleship.on()
def start_turn():
    s = input('Your move> ')

    for char in s:
        if char.isdigit():
            global current_x
            current_x = int(char) - 1
        elif char.isupper():
            global current_y
            current_y = ord(char) - 65
        elif char.islower():
            global current_y
            current_y = ord(char) - 97
        else:
            print('Invalid Character')

    battleship.attack(s)


@battleship.on()
def hit():
    print('You hit the target!')
    playerGrid[current_y][current_x] = 'X'


@battleship.on()
def miss():
    print('Aww.. You missed!')
    enemyGrid[current_y][current_x] = 'O'


@battleship.on()
def win():
    print('Yay! You won!')
    playerGrid[current_y][current_x] = 'X'
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
    for char in vector:
        if char.isdigit():
            enemy_x = char - 1
        elif char.isupper():
            enemy_y = ord(char) - 65
        elif char.islower():
            enemy_y = ord(char) - 97
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
