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

    # method that checks ensuing places ship is placed are all free
    def check_spaces(self):
        try:
            all_clear = True
            if self.orientation == 'V':
                for i in range(1, self.space):
                    if self.playerBoard[self.coordinate + 10 * i] != "0":
                        all_clear = False
            elif self.orientation == 'H':
                for i in range(1, self.space):
                    if self.playerBoard[self.coordinate + i] != "0":
                        all_clear = False
            while not all_clear:
                self.coordinate = int(input('That piece falls on top of another. Pick another coordinate: '))
                all_clear = True
                self.check_spaces()
        except:
            self.coordinate = int(input('The piece you entered fell off the edge. Pick another coordinate: '))
            self.check()
            return

    # method that puts together all other methods
    def check(self):
        self.coordinate = self.check_coord()
        self.orientation = self.check_orient()
        self.check_spaces()
