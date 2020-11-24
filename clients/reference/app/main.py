import os
import threading
import time
from client import Battleship
import Grid
import Ship

grpc_host = os.getenv('GRPC_HOST', 'localhost')
grpc_port = os.getenv('GRPC_PORT', '50051')

playing = threading.Event()
playing.set()

battleship = Battleship(grpc_host=grpc_host, grpc_port=grpc_port)
player1 = Grid.GridTable.grid1
player2 = Grid.GridTable.grid2

my_attack = "a"


def clear():
    print("\n" * 100)


@battleship.on()
def begin():
    print('Game started!')


@battleship.on()
def start_turn():
    print("\n")
    s = input('Your move> ')
    global my_attack
    my_attack = s
    battleship.attack(s)


@battleship.on()
def hit():
    row = my_attack[0].upper()
    col = int(my_attack[1:]) - 1
    for key in player2:
        if key == row:
            player2[key].pop(col)
            player2[key].insert(col, 'Hit')
    clear()
    Grid.display_grid(player1, player2)
    print('\n\nYou hit the target!')


@battleship.on()
def miss():
    row = my_attack[0].upper()
    col = int(my_attack[1:]) - 1
    for key in player2:
        if key == row:
            player2[key].pop(col)
            player2[key].insert(col, 'Miss')
    clear()
    Grid.display_grid(player1, player2)
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
    position = vector[0].upper()
    row = position[0]
    col = int(position[1:]) - 1
    if row in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
        print(col)
        print(f"\n Shot received at {position}")
        count = 0
        for item in player1[row]:
            count += 1
            if count == col + 1:
                if item == " " or item == "Miss" or item == "Hit":
                    player1[row][col] = "Miss"
                    """Send Miss event"""
                    battleship.miss()
                else:
                    player1[row][col] = "Hit"
                    """Send Hit Or Defeat Event"""
                    Grid.display_grid(player1, player2)
                    print("""\n\nAll Ships Sunk? Y/N""")
                    answer = input("Enter Y or N: ")
                    if answer[0].upper() == 'Y':
                        battleship.defeat()
                    else:
                        battleship.hit()
        Grid.display_grid(player1, player2)
    else:
        Grid.display_grid(player1, player2)
        print(f"\nEnemy sending attack coordinate outside of grid value :::{vector[0]}")
        battleship.miss()


if __name__ == '__main__':
    Grid.display_grid(player1, player2)
    player_table = Ship.placement(player1, player2)
    Grid.display_grid(player_table, player2)

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
