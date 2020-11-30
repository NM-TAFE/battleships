import os
import threading
import time
from reference.app.client import Battleship
from clients.KelsonD.board import Board

grpc_host = os.getenv('GRPC_HOST', 'localhost')
grpc_port = os.getenv('GRPC_PORT', '50051')

playing = threading.Event()
playing.set()
battleship = Battleship(grpc_host=grpc_host, grpc_port=grpc_port)
game = Board()


@battleship.on()
def begin():
    print('Game started!')


@battleship.on()
def start_turn():
    s = game.my_turn()
    battleship.attack(s)


@battleship.on()
def hit():
    print('You hit the target!')
    game.update_hit_board('hit', coord)


@battleship.on()
def miss():
    print('Aww.. You missed!')
    game.update_hit_board('miss', coord)


@battleship.on()
def win():
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
    while True:
        print("""H)it, m)iss, or d)efeat?""")
        s = game.check_strike()
        if len(s):
            if s == 'hit':
                battleship.hit()
                break
            elif s == 'miss':
                battleship.miss()
                break
            elif game.check_defeat():
                battleship.defeat()
                break


print('Waiting for the game to start...')
battleship.join()
while playing.is_set():
    time.sleep(1.0)