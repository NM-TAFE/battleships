class Board:
    def __init__(self):
        self.playerBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def check_strike(self, attack):
        if (99 < attack >= 0) or (self.playerBoard[attack] == "X"):
            return "invalid"
        if self.playerBoard[attack] == "0":
            return "miss"
        if self.playerBoard[attack] == "S":
            self.playerBoard[attack] = "X"
            return "hit"

    #def check_placement(self, cord, orient, ship):

    # method used to populate board with ships
    # prompts user to input number indicating where ship should go and then places ship accordingly
    # TODO: create a loop to go through prompts to place ships
    def place_ships(self):
        print("When placing ships, indicate where on the board you would like your ship to be" + "\n" +
              "by entering an integer from 0 to 99.")
        print("After this you will be prompted to enter an H or V to indicate if you want the ship to " + "\n" +
              "be placed horizontally or vertically")
        print("The ship will be placed going down from the selected coordinate if vertical," + "\n" +
              "and to the right if horizontal.")
        carrier_coord = int(input("Select carrier position"))
        battleship_coord = int(input("Select battleship position (0-99): "))
        battleship_orient = int(input("Select orientation (H/V): "))
        sub1_coord = int(input("Select submarine position(0-99): "))
        sub1_orient = int(input("Select orientation (H/V): "))
        sub2_coord = int(input("Select second submarine position(0-99): "))
        sub2_orient = int(input("Select orientation (H/V): "))
        sub3_coord = int(input("Select third submarine position(0-99): "))
        sub3_orient = int(input("Select orientation (H/V): "))
        cruiser_coord = int(input("Select cruiser position (0-99): "))
        cruiser_orient = int(input("Select orientation (H/V): "))
        destroyer1_coord = int(input("Select destroyer position(0-99): "))
        destroyer1_orient = int(input("Select orientation (H/V): "))
        destroyer2_coord = int(input("Select second destroyer position(0-99): "))
        destroyer2_orient = int(input("Select orientation (H/V): "))
        ptboat1_coord = int(input("Select patrol boat position(0-99): "))
        ptboat1_orient = int(input("Select orientation (H/V): "))
        ptboat2_coord = int(input("Select second patrol boat position(0-99): "))
        ptboat2_orient = int(input("Select orientation (H/V): "))


    # method that checks if a space a player requests for a piece is free
    # returns false if space is occupied and true if it is free
    def check_free(self, coord, orientation, spaces):
        is_free = True;
        if self.playerBoard[coord] == 0 and orientation == "V":
            for i in range(1, spaces):
                if self.playerBoard[coord+10*i] == "S":
                    is_free = False
        elif self.playerBoard[coord] == 0 and orientation == "H":
            for i in range(1, spaces):
                if self.playerBoard[coord+i] == "S":
                    is_free = False
        return is_free



    # method that checks for a win and takes the board as an input
    # returns false if a win does not occur and true if one does
    def check_win(self, board):
        ship_left = False
        for space in board:
            if space == "S":
                ship_left = True
        if ship_left:
            return False
        else:
            return True
