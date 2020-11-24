from colorama import Fore, Back, Style
from clients.reference.app.validator import MoveValidator


class Board:
    def __init__(self):
        self.playerBoard = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                            "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                            "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                            "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                            "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                            "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                            "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                            "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                            "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                            "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        self.hitBoard = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                         "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                         "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                         "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                         "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                         "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                         "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                         "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                         "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
                         "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

    def get_boards(self):
        return self.playerBoard, self.hitBoard

    # method that takes index of hits as input and displays it in a board
    def draw_board(self, board):
        print("      00 |01 |02 |03 |04 |05 |06 |07 |08 |09  ")
        print("----------------------------------------------")
        print(" 00 ||" + Fore.RED + Back.BLUE + " " + self.playerBoard[0] + " | " +
              self.playerBoard[1] + " | " + self.playerBoard[2] + " | " + self.playerBoard[3] + " | " +
              self.playerBoard[4] + " | " + self.playerBoard[5] + " | " + self.playerBoard[6] + " | " +
              self.playerBoard[7] + " | " + self.playerBoard[8] + " | " + self.playerBoard[9] + "  " + Style.RESET_ALL)
        print(" 10 ||" + Fore.RED + Back.BLUE + " " + self.playerBoard[10] + " | " +
              self.playerBoard[11] + " | " + self.playerBoard[12] + " | " + self.playerBoard[13] + " | " +
              self.playerBoard[14] + " | " + self.playerBoard[15] + " | " + self.playerBoard[16] + " | " +
              self.playerBoard[17] + " | " + self.playerBoard[18] + " | " + self.playerBoard[
                  19] + "  " + Style.RESET_ALL)
        print(" 02 ||" + Fore.RED + Back.BLUE + " " + self.playerBoard[20] + " | " +
              self.playerBoard[21] + " | " + self.playerBoard[22] + " | " + self.playerBoard[23] + " | " +
              self.playerBoard[24] + " | " + self.playerBoard[25] + " | " + self.playerBoard[26] + " | " +
              self.playerBoard[27] + " | " + self.playerBoard[28] + " | " + self.playerBoard[
                  29] + "  " + Style.RESET_ALL)
        print(" 30 ||" + Fore.RED + Back.BLUE + " " + self.playerBoard[30] + " | " +
              self.playerBoard[31] + " | " + self.playerBoard[32] + " | " + self.playerBoard[33] + " | " +
              self.playerBoard[34] + " | " + self.playerBoard[35] + " | " + self.playerBoard[36] + " | " +
              self.playerBoard[37] + " | " + self.playerBoard[38] + " | " + self.playerBoard[
                  39] + "  " + Style.RESET_ALL)
        print(" 40 ||" + Fore.RED + Back.BLUE + " " + self.playerBoard[40] + " | " +
              self.playerBoard[41] + " | " + self.playerBoard[42] + " | " + self.playerBoard[43] + " | " +
              self.playerBoard[44] + " | " + self.playerBoard[45] + " | " + self.playerBoard[46] + " | " +
              self.playerBoard[47] + " | " + self.playerBoard[48] + " | " + self.playerBoard[
                  49] + "  " + Style.RESET_ALL)
        print(" 50 ||" + Fore.RED + Back.BLUE + " " + self.playerBoard[50] + " | " +
              self.playerBoard[51] + " | " + self.playerBoard[52] + " | " + self.playerBoard[53] + " | " +
              self.playerBoard[54] + " | " + self.playerBoard[55] + " | " + self.playerBoard[56] + " | " +
              self.playerBoard[57] + " | " + self.playerBoard[58] + " | " + self.playerBoard[
                  59] + "  " + Style.RESET_ALL)
        print(" 60 ||" + Fore.RED + Back.BLUE + " " + self.playerBoard[60] + " | " +
              self.playerBoard[61] + " | " + self.playerBoard[62] + " | " + self.playerBoard[63] + " | " +
              self.playerBoard[64] + " | " + self.playerBoard[65] + " | " + self.playerBoard[66] + " | " +
              self.playerBoard[67] + " | " + self.playerBoard[68] + " | " + self.playerBoard[
                  69] + "  " + Style.RESET_ALL)
        print(" 70 ||" + Fore.RED + Back.BLUE + " " + self.playerBoard[70] + " | " +
              self.playerBoard[71] + " | " + self.playerBoard[72] + " | " + self.playerBoard[73] + " | " +
              self.playerBoard[74] + " | " + self.playerBoard[75] + " | " + self.playerBoard[76] + " | " +
              self.playerBoard[77] + " | " + self.playerBoard[78] + " | " + self.playerBoard[
                  79] + "  " + Style.RESET_ALL)
        print(" 80 ||" + Fore.RED + Back.BLUE + " " + self.playerBoard[80] + " | " +
              self.playerBoard[81] + " | " + self.playerBoard[82] + " | " + self.playerBoard[83] + " | " +
              self.playerBoard[84] + " | " + self.playerBoard[85] + " | " + self.playerBoard[86] + " | " +
              self.playerBoard[87] + " | " + self.playerBoard[88] + " | " + self.playerBoard[
                  89] + "  " + Style.RESET_ALL)
        print(" 90 ||" + Fore.RED + Back.BLUE + " " + self.playerBoard[90] + " | " +
              self.playerBoard[91] + " | " + self.playerBoard[92] + " | " + self.playerBoard[93] + " | " +
              self.playerBoard[94] + " | " + self.playerBoard[95] + " | " + self.playerBoard[96] + " | " +
              self.playerBoard[97] + " | " + self.playerBoard[98] + " | " + self.playerBoard[
                  99] + "  " + Style.RESET_ALL)

    def check_strike(self, attack):
        if (99 < attack >= 0) or (self.playerBoard[attack] == "X"):
            return "invalid"
        if self.playerBoard[attack] == "0":
            return "miss"
        if self.playerBoard[attack] == "S":
            self.playerBoard[attack] = "X"
            return "hit"

    # method used to populate board with ships
    # prompts user to input number indicating where ship should go and then places ship accordingly using place_piece method
    # TODO: create a loop to go through prompts to place ships
    def place_ships(self):
        print("When placing ships, indicate where on the board you would like your ship to be" + "\n" +
              "by entering an integer from 0 to 99.")
        print("After this you will be prompted to enter an H or V to indicate if you want the ship to " + "\n" +
              "be placed horizontally or vertically")
        print("The ship will be placed going down from the selected coordinate if vertical," + "\n" +
              "and to the right if horizontal.")
        carrier_coord = int(input("Select carrier position (0-99): "))
        carrier_orient = str(input("Select carrier orientation (H/V): "))
        self.place_piece(carrier_coord, carrier_orient, 5)
        battleship_coord = int(input("Select battleship position (0-99): "))
        battleship_orient = str(input("Select orientation (H/V): "))
        self.place_piece(battleship_coord, battleship_orient, 4)
        sub1_coord = int(input("Select submarine position(0-99): "))
        sub1_orient = str(input("Select orientation (H/V): "))
        self.place_piece(sub1_coord, sub1_orient, 3)
        sub2_coord = int(input("Select second submarine position(0-99): "))
        sub2_orient = str(input("Select orientation (H/V): "))
        self.place_piece(sub2_coord, sub2_orient, 3)
        sub3_coord = int(input("Select third submarine position(0-99): "))
        sub3_orient = str(input("Select orientation (H/V): "))
        self.place_piece(sub3_coord, sub3_orient, 3)
        cruiser_coord = int(input("Select cruiser position (0-99): "))
        cruiser_orient = str(input("Select orientation (H/V): "))
        self.place_piece(cruiser_coord, cruiser_orient, 3)
        destroyer1_coord = int(input("Select destroyer position(0-99): "))
        destroyer1_orient = str(input("Select orientation (H/V): "))
        self.place_piece(destroyer1_coord, destroyer1_orient, 2)
        destroyer2_coord = int(input("Select second destroyer position(0-99): "))
        destroyer2_orient = str(input("Select orientation (H/V): "))
        self.place_piece(destroyer2_coord, destroyer2_orient, 2)
        ptboat1_coord = int(input("Select patrol boat position(0-99): "))
        ptboat1_orient = str(input("Select orientation (H/V): "))
        self.place_piece(ptboat1_coord, ptboat1_orient, 1)
        ptboat2_coord = int(input("Select second patrol boat position(0-99): "))
        ptboat2_orient = str(input("Select orientation (H/V): "))
        self.place_piece(ptboat2_coord, ptboat2_orient, 1)
        return self.playerBoard

    def check_coord(self, coordinate):
        while coordinate < 0 or coordinate > 99 or self.playerBoard[coordinate] == "■":
            coordinate = int(input("Please enter a coordinate that is in range: "))
            coordinate = self.check_coord(coordinate)
            return coordinate
        else:
            return coordinate

    def check_orient(self, orient):
        while orient not in {'H', 'V'}:
            orient = str(input("Please enter an orientation that is H)orizontal or V)ertical: "))
            orient = self.check_orient(orient)
            return orient
        else:
            return orient

    def check_surrounding(self, coord, orient, spaces):
        coord = self.check_coord(coord)
        orient = self.check_orient(orient)
        if orient == "V":
            for i in range(1, spaces):
                if self.playerBoard[coord + 10 * i] == "■":
                    coord = int(input("That overlaps with an existing piece, please select another coordinate: "))
                    coord, orient = self.check_surrounding(coord, orient, spaces)
                else:
                    return coord, orient
        else:
            for i in range(1, spaces):
                if self.playerBoard[coord + i] == "■":
                    coord = int(input("That overlaps with an existing piece, please select another coordinate: "))
                    coord, orient = self.check_surrounding(coord, orient, spaces)
                    return coord, orient

    # method that places a piece on the board
    def place_piece(self, coord, orientation, spaces):
        # create MoveValidator class and pass information to check the moves are okay
        valid = MoveValidator(coord, orientation, spaces, self.playerBoard)
        # check the moves
        valid.check_surrounding()
        # save the valid moves once they've been checked
        valid_coord = valid.coordinate
        valid_orient = valid.orientation
        self.playerBoard[valid_coord] = "■"
        if valid_orient == "H":
            for i in range(1, spaces):
                self.playerBoard[coord + i] = "■"
        elif valid_orient == "V":
            for i in range(1, spaces):
                self.playerBoard[coord + 10 * i] = "■"
        self.draw_board(self.playerBoard)

    # method that checks for a win and takes the board as an input
    # returns false if a win does not occur and true if one does
    def check_win(self, board):
        ship_left = False
        for space in board:
            if space == "■":
                ship_left = True
        if ship_left:
            return False
        else:
            return True


if __name__ == '__main__':
    game = Board()
    game.place_ships()
