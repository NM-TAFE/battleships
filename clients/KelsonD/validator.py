import math


class MoveValidator:

    # class takes coordinates, orient, spaces, and board as constructors
    def __init__(self, coord, orient, spaces, board):
        self.coordinate = coord
        self.orientation = orient
        self.space = spaces
        self.playerBoard = board

    # method that checks the user enters a valid input for orientation
    def check_coord(self):
        while self.coordinate < 0 or self.coordinate > 99 or self.playerBoard[self.coordinate] == "■":
            self.coordinate = int(input("Please enter a coordinate that is in range and free: "))
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

    # method that checks ensuing places ship is placed are all free
    def check_spaces(self):
        try:
            # checks if any following spots fall on existing piece in vertical
            if self.orientation == 'V':
                for i in range(1, self.space):
                    if self.playerBoard[self.coordinate + 10 * i] != "0":
                        self.coordinate = int(input("Piece falls on another. Please pick another coordinate: "))
                        self.check_spaces()
            # checks if any following spots fall on existing piece in horizontal
            elif self.orientation == 'H':
                for i in range(1, self.space):
                    if self.playerBoard[self.coordinate + i] != "0":
                        self.coordinate = int(input("Piece falls on another. Please pick another coordinate: "))
                        self.check_spaces()
        # catch when user enters coordinate out of range
        except:
            self.coordinate = int(input('The piece you entered fell off the edge. Pick another coordinate: '))
            self.check_spaces()
            return

    # method to check if piece attempts to wrap around board
    def wrap_around(self):
        if self.orientation == 'H':
            start_coord = int(self.coordinate) + 1
            end_coord = int(self.coordinate) + int(self.space)
            for i in range(start_coord, end_coord):
                # if first digit of coord does not match first digit of next placement makes user re enter
                if math.floor(i/10) != math.floor((i - 1) / 10):
                    self.coordinate = int(input("Piece falls off the edge. Pick another coordinate: "))
                    self.wrap_around()

    # method that puts together all other methods
    def check(self):
        self.coordinate = self.check_coord()
        self.orientation = self.check_orient()
        self.check_spaces()
        self.wrap_around()
