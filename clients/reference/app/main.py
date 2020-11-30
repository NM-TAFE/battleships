import os
import threading
import time
from client import Battleship

from clients.reference.app.Board.board import Board

grpc_host = os.getenv('GRPC_HOST', 'localhost')
grpc_port = os.getenv('GRPC_PORT', '50051')

playing = threading.Event()
playing.set()

battleship = Battleship(grpc_host=grpc_host, grpc_port=grpc_port)

# Override methods here!
# Instantiate 1 player board each here
# Instantiate 1 View Board each


player = Board()
opponentTargeting = Board(True)  # Empty Board


@battleship.on()
def begin():
    print('Game started!')


@battleship.on()
def start_turn():
    print("\n")
    shot = "myboard"  # TODO: Maybe .upper input somehow and change coord parser?
    while shot == "myboard":
        shot = input('Type myboard to see OWN playerboard\n OR enter a grid position e.g. A3> ')
        player.displayCurrentBoard()
        print("\n")
    global shotTracer  # We need to do this to pass this parameter to hit or miss functions otherwise we have
    # overloaded it as it is not expecting any parameters
    shotTracer = shot
    battleship.attack(shot)


@battleship.on()
def hit():
    # Mark Opponent Targeting Board, This is receiving feedback from start turn's attack if hit
    opponentTargeting.markTargetShot(shotTracer, "X")
    opponentTargeting.displayCurrentBoard()
    print(f'You hit the target!')
    print("\n")
    time.sleep(2)
    print("Waiting for Opponent's Turn")
    print("\n")


@battleship.on()
def miss():
    # Mark Opponent Board, This is receiving feedback from start turn's attack if miss
    opponentTargeting.markTargetShot(shotTracer, "*")
    opponentTargeting.displayCurrentBoard()
    print('Aww.. You missed!')
    print("\n")
    time.sleep(2)
    print("Waiting for Opponent's Turn")
    print("\n")


@battleship.on()
def win():
    print('Yay! You won!')
    playing.clear()


@battleship.on()
def lose():
    print('Aww... You lost...')
    playing.clear()
    battleship.defeat()


# Code board objects method to return ship counter and if any playersboards 0 ships left end game
@battleship.on()
def attack(unfilteredShot):
    # This is receiving player

    shot = unfilteredShot[0]
    print(f'Shot received at {shot}')
    hitFeedback = player.receiveShot(shot)

    print(f"{hitFeedback} received at vector {shot}!")

    if hitFeedback == "HIT":
        player.minusShipSquare()  # Starts at 26, when 0, defeated
        defeated = player.endCheck()
        print(f"You have {player.totalShipSquares} before your fleet is destroyed!!!")
        if defeated:
            battleship.defeat()

        battleship.hit()

    else:
        battleship.miss()


if __name__ == "__main__":
    print("Prejoin phase has started")
    string_quickPlace = input(
        "Automatic ship placement? yes or no: ").upper()  # No fancy randomizer for ships, just a prefilled board
    if string_quickPlace == "YES":
        player.placingShips(True)
    else:
        player.placingShips(False)
    print('Waiting for the game to start...')
    battleship.join()
    while playing.is_set():
        time.sleep(1.0)
