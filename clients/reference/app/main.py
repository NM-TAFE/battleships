import os
import threading
import time
from client import Battleship
from audioplayer import AudioPlayer


grpc_host = os.getenv('GRPC_HOST', 'localhost')
grpc_port = os.getenv('GRPC_PORT', '50051')

playing = threading.Event()
playing.set()

battleship = Battleship(grpc_host=grpc_host, grpc_port=grpc_port)

# Added a background track to play during gameplay
AudioPlayer("clients/reference/app/sounds/backgroundtrack.mp3").play(loop=True)

@battleship.on()
def begin():
    print('Game started!')


@battleship.on()
def start_turn():
    s = input('Your move> ')
    battleship.attack(s)


@battleship.on()
def hit():
    AudioPlayer("clients/reference/app/sounds/hit.mp3").play(block=False) #plays the hit sound
    print('You hit the target!')


@battleship.on()
def miss():
    AudioPlayer("clients/reference/app/sounds/miss.mp3").play(block=False) #plays the miss sound
    print('Aww.. You missed!')


@battleship.on()
def win():
    print('Yay! You won!')
    playing.clear()


@battleship.on()
def lose():
    print('Aww... You lost...')
    AudioPlayer("clients/reference/app/sounds/defeat.mp3").play(block=False) #plays the defeat sound
    playing.clear()


@battleship.on()
def attack(vector):
    vector = vector[0]
    print(f'Shot received at {vector}')
    while True:
        print("""H)it, m)iss, or d)efeat?""")
        s = input('Enter status> ')
        _s = s[0].upper()
        if _s == 'H':
            battleship.hit()
            break
        elif _s == 'M':
            battleship.miss()
            break
        elif _s == 'D':
            battleship.defeat()
            break
        else:
            continue


print('Waiting for the game to start...')
battleship.join()
while playing.is_set():
    time.sleep(1.0)
