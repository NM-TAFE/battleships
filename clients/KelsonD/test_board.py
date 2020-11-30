from clients.KelsonD.board import Board

""".py file to test some of the methods of the Board class, such as placing ships in the console.
This is useful for if the user wishes to see how the initial setup would work but is unable to
get access to internet or a working server."""

test_game = Board()

if __name__ == '__main__':
    test_game.place_ships()