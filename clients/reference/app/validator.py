class MoveValidator:

    def __init__(self, coord, orient, spaces, board):
        self.coordinate = coord
        self.orientation = orient
        self.space = spaces
        self.playerBoard = board

    # method that checks the user enters a valid input for orientation
    def check_coord(self):
        while self.coordinate < 0 or self.coordinate > 99 or self.playerBoard[self.coordinate] == "■":
            self.coordinate = int(input("Please enter a coordinate that is in range: "))
            self.coordinate = self.check_coord()
            return self.coordinate
        else:
            return self.coordinate

    # method that checks the user entered a valid character for orientation
    def check_orient(self):
        while self.orientation not in {'H', 'V'}:
            self.orientation = str(input("Please enter an orientation that is H)orizontal or V)ertical: "))
            self.orientation = self.check_orient()
            return self.orientation
        else:
            return self.orientation

    #
    def check_spaces(self):
        if self.orientation == 'V':
            for i in range(1, self.space):
                if self.playerBoard[self.coordinate + 10*i] == "■":
                    return False
            else:
                return True
        elif self.orientation == 'H':
            for i in range(1, self.space):
                if self.playerBoard[self.coordinate + i] == "■":
                    return False
            else:
                return True

    # method that checks all following places piece is put are valid
    def check_surrounding(self):
        self.coordinate = self.check_coord()
        self.orientation = self.check_orient()
        while not self.check_spaces():
            self.coordinate = int(input('Location overlaps with piece, select another coordinate: '))
            self.check_spaces()
