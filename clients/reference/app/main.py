import os
import threading
import time
from clients.reference.client.py import Battleship
from clients.reference.app.board import Board

grpc_host = os.getenv('GRPC_HOST', 'localhost')
grpc_port = os.getenv('GRPC_PORT', '50051')

playing = threading.Event()
playing.set()

battleship = Battleship(grpc_host=grpc_host, grpc_port=grpc_port)

game = Board()


@battleship.on()
def begin():
    """This callback is called when the game server indicates that a game
    starts. This happens when two players are available to play. If you are
    the first to register, you may have to wait for someone else to connect.
    """
    print('Game started!')


@battleship.on()
def start_turn():
    s = game.my_turn()
    battleship.attack(s)


@battleship.on()
def hit():
    print('You hit the target!')


@battleship.on()
def miss():
    print('Aww.. You missed!')


@battleship.on()
def win():
    """This callback indicates the other player was defeated.
    """
    print('Yay! You won!')
    playing.clear()


@battleship.on()
def lose():
    """Callback indicates you are defeated. This callback is called when you
    call :meth: 'defeat' method on the Battleship client, so this will never
    come as a surprise.
    """
    print('Aww... You lost...')
    playing.clear()


@battleship.on()
def attack(vector):
    """Callback indicates an attack by another player. It takes a single
    argument which is the square that is attacked. Please note game server
    does not validate the vector, so it is up to the clients to decide on a
    certain format.
    """
    vector = vector[0]
    print(f'Shot received at {vector}')
    while True:
        # print("""H)it, m)iss, or d)efeat?""")
        s = game.check_strike(vector)
        if s == 'hit':
            battleship.hit()
            game.update_hit_board(s, vector)
            break
        elif s == 'miss':
            battleship.miss()
            game.update_hit_board(s, vector)
            break
        elif game.check_defeat():
            battleship.defeat()
            break
        else:
            continue


game.place_ships()
print('Waiting for the game to start...')
battleship.join()
while playing.is_set():
    # giving processor a break
    time.sleep(1.0)
