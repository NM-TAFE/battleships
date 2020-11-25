import os
import threading
import time

from client import Battleship

<<<<<<< HEAD
from clients.reference.app.Board import ship
from clients.reference.app.Board import board

grpc_host = os.getenv('GRPC_HOST', 'localhost')
=======
grpc_host = os.getenv('GRPC_HOST', 'b.sndm.me')
>>>>>>> 6883eedf3b53ed8d5cbbda19237b89536d06758d
grpc_port = os.getenv('GRPC_PORT', '50051')


playing = threading.Event()
playing.set()

battleship = Battleship(grpc_host=grpc_host, grpc_port=grpc_port)


@battleship.on()
def begin():
    print('Game started!')


@battleship.on()
def start_turn():
    s = input('Your move> ')
    battleship.attack(s)


@battleship.on()
def hit():
    print('\n\nYou hit the target!')


@battleship.on()
def miss():
    print('\n\nAww.. You missed!')


@battleship.on()
def win():
    print('\n\nYay! You won!')
    playing.clear()


@battleship.on()
def lose():
    print('\n\nAww... You lost...')
    playing.clear()


@battleship.on()
def attack(vector):
    vector = vector[0]
    print(f'Shot received at {vector}')
    while True:
        print("""H)it, m)iss, or d)efeat?""")
        s = input('Enter status> ')
        if len(s):
            _s = s[0].upper()
            if _s == 'H':
                battleship.hit()
<<<<<<< HEAD
        board.display_grid(player1, player2)
    else:
        board.display_grid(player1, player2)
        print(f"\nEnemy sending attack coordinate outside of grid value :::{vector[0]}")
        battleship.miss()


if __name__ == '__main__':
    board.display_grid(player1, player2)
    player_table = ship.placement(player1, player2)
    board.display_grid(player_table, player2)
    while True:
        s = input("\nReady to join? Y/N : ")
        if s[0].upper() == 'Y':
            break
        else:
            continue
    print('\nWaiting for the game to start...')
    battleship.join()
    while playing.is_set():
        time.sleep(1.0)
=======
                break
            elif _s == 'M':
                battleship.miss()
                break
            elif _s == 'D':
                battleship.defeat()
                break

                
print('\nWaiting for the game to start...')
battleship.join()
while playing.is_set():
    time.sleep(1.0)
>>>>>>> 6883eedf3b53ed8d5cbbda19237b89536d06758d
