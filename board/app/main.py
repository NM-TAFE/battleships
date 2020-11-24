import Grid
import Ship


def clear():
    print("\n" * 100)


def miss(position):
    row = position[0]
    col = int(position[1:]) - 1
    for key in player2:
        if key == row:
            player2[key].pop(col)
            player2[key].insert(col, 'Miss')
    clear()
    Grid.display_grid(player1, player2)


def hit(position):
    row = position[0]
    col = int(position[1:]) - 1
    for key in player2:
        if key == row:
            player2[key].pop(col)
            player2[key].insert(col, 'Hit')
    clear()
    Grid.display_grid(player1, player2)


def attacked(position):
    row = position[0]
    col = int(position[1:]) - 1
    count = 0
    for item in player1[row]:
        count += 1
        if count == col + 1:
            if item == " " or item == "X":
                player1[row].pop(col)
                player1[row].insert(col, "Miss")
                """Send Miss event"""
                print("\nMiss")
            else:
                player1[row].pop(col)
                player1[row].insert(col, "Hit")
                """Send Hit event"""
                print("\nHit")
    Grid.display_grid(player1, player2)


player1 = Grid.GridTable.grid1
player2 = Grid.GridTable.grid2


if __name__ == '__main__':
    Grid.display_grid(player1, player2)
    player_table = Ship.placement(player1, player2)
    Grid.display_grid(player_table, player2)
    attacked("A5")
    hit("D6")
    attacked("A4")
    miss("C6")
    attacked("B4")
    hit("D7")

