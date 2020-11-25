from colorama import Fore, Back, Style

from clients.reference.app.validator import MoveValidator


class Board:
    def __init__(self):
        # board that stores your ship placement
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
        # board that stores shots you have submitted
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


    # method that takes index of hits as input and displays it in a board
    def draw_player_board(self):
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

    # method that draws the board that records hit record
    # method that takes index of hits as input and displays it in a board
    def draw_hit_board(self):
        print("      00 |01 |02 |03 |04 |05 |06 |07 |08 |09  ")
        print("----------------------------------------------")
        print(" 00 ||" + Fore.RED + Back.BLUE + " " + self.hitBoard[0] + " | " +
              self.hitBoard[1] + " | " + self.hitBoard[2] + " | " + self.hitBoard[3] + " | " +
              self.hitBoard[4] + " | " + self.hitBoard[5] + " | " + self.hitBoard[6] + " | " +
              self.hitBoard[7] + " | " + self.hitBoard[8] + " | " + self.hitBoard[9] + "  " + Style.RESET_ALL)
        print(" 10 ||" + Fore.RED + Back.BLUE + " " + self.hitBoard[10] + " | " +
              self.hitBoard[11] + " | " + self.hitBoard[12] + " | " + self.hitBoard[13] + " | " +
              self.hitBoard[14] + " | " + self.hitBoard[15] + " | " + self.hitBoard[16] + " | " +
              self.hitBoard[17] + " | " + self.hitBoard[18] + " | " + self.hitBoard[19] + "  " + Style.RESET_ALL)
        print(" 02 ||" + Fore.RED + Back.BLUE + " " + self.hitBoard[20] + " | " +
              self.hitBoard[21] + " | " + self.hitBoard[22] + " | " + self.hitBoard[23] + " | " +
              self.hitBoard[24] + " | " + self.hitBoard[25] + " | " + self.hitBoard[26] + " | " +
              self.hitBoard[27] + " | " + self.hitBoard[28] + " | " + self.hitBoard[29] + "  " + Style.RESET_ALL)
        print(" 30 ||" + Fore.RED + Back.BLUE + " " + self.hitBoard[30] + " | " +
              self.hitBoard[31] + " | " + self.hitBoard[32] + " | " + self.hitBoard[33] + " | " +
              self.hitBoard[34] + " | " + self.hitBoard[35] + " | " + self.hitBoard[36] + " | " +
              self.hitBoard[37] + " | " + self.hitBoard[38] + " | " + self.hitBoard[39] + "  " + Style.RESET_ALL)
        print(" 40 ||" + Fore.RED + Back.BLUE + " " + self.hitBoard[40] + " | " +
              self.hitBoard[41] + " | " + self.hitBoard[42] + " | " + self.hitBoard[43] + " | " +
              self.hitBoard[44] + " | " + self.hitBoard[45] + " | " + self.hitBoard[46] + " | " +
              self.hitBoard[47] + " | " + self.hitBoard[48] + " | " + self.hitBoard[49] + "  " + Style.RESET_ALL)
        print(" 50 ||" + Fore.RED + Back.BLUE + " " + self.hitBoard[50] + " | " +
              self.hitBoard[51] + " | " + self.hitBoard[52] + " | " + self.hitBoard[53] + " | " +
              self.hitBoard[54] + " | " + self.hitBoard[55] + " | " + self.hitBoard[56] + " | " +
              self.hitBoard[57] + " | " + self.hitBoard[58] + " | " + self.hitBoard[59] + "  " + Style.RESET_ALL)
        print(" 60 ||" + Fore.RED + Back.BLUE + " " + self.hitBoard[60] + " | " +
              self.hitBoard[61] + " | " + self.hitBoard[62] + " | " + self.hitBoard[63] + " | " +
              self.hitBoard[64] + " | " + self.hitBoard[65] + " | " + self.hitBoard[66] + " | " +
              self.hitBoard[67] + " | " + self.hitBoard[68] + " | " + self.hitBoard[69] + "  " + Style.RESET_ALL)
        print(" 70 ||" + Fore.RED + Back.BLUE + " " + self.hitBoard[70] + " | " +
              self.hitBoard[71] + " | " + self.hitBoard[72] + " | " + self.hitBoard[73] + " | " +
              self.hitBoard[74] + " | " + self.hitBoard[75] + " | " + self.hitBoard[76] + " | " +
              self.hitBoard[77] + " | " + self.hitBoard[78] + " | " + self.hitBoard[79] + "  " + Style.RESET_ALL)
        print(" 80 ||" + Fore.RED + Back.BLUE + " " + self.playerBoard[80] + " | " +
              self.hitBoard[81] + " | " + self.hitBoard[82] + " | " + self.hitBoard[83] + " | " +
              self.hitBoard[84] + " | " + self.hitBoard[85] + " | " + self.hitBoard[86] + " | " +
              self.hitBoard[87] + " | " + self.hitBoard[88] + " | " + self.hitBoard[89] + "  " + Style.RESET_ALL)
        print(" 90 ||" + Fore.RED + Back.BLUE + " " + self.playerBoard[90] + " | " +
              self.hitBoard[91] + " | " + self.hitBoard[92] + " | " + self.hitBoard[93] + " | " +
              self.hitBoard[94] + " | " + self.hitBoard[95] + " | " + self.hitBoard[96] + " | " +
              self.hitBoard[97] + " | " + self.hitBoard[98] + " | " + self.hitBoard[99] + "  " + Style.RESET_ALL)

    # method to receive player moves
    def my_turn(self):
        guess = str(input("Enter a coordinate to shoot at: "))
        return guess

    # checks if opponents
    def check_strike(self, attack):
        if (99 < attack >= 0) or (self.playerBoard[attack] == "■") or (self.playerBoard[attack == 'M']):
            return 'invalid'
        if self.playerBoard[attack] == "0":
            self.playerBoard[attack] = 'M'
            return 'miss'
        if self.playerBoard[attack] == "■":
            self.playerBoard[attack] = "X"
            return 'hit'

    # method to update players hit board to log attacks
    def update_hit_board(self, feedback, coord):
        if feedback == 'hit':
            print('Shot was a hit!!!')
            self.hitBoard[coord] = 'H'
            self.draw_hit_board()
        if feedback == 'miss':
            print('Shot was a miss... :(')
            self.hitBoard[coord] = 'M'
            self.draw_hit_board()
        if feedback == 'invalid':
            print("Location out of range or already guessed.")
            self.my_turn()

    # method used to populate board with ships
    # prompts user to input number indicating where ship should go and places ship accordingly using place_piece
    # TODO: create a loop to go through prompts to place ships
    def place_ships(self):
        # instructions
        print("When placing ships, indicate where on the board you would like your ship to be" + "\n" +
              "by entering an integer from 0 to 99.")
        print("After this you will be prompted to enter an H or V to indicate if you want the ship to " + "\n" +
              "be placed horizontally or vertically")
        print("The ship will be placed going down from the selected coordinate if vertical," + "\n" +
              "and to the right if horizontal.")
        # place carrier
        carrier_coord = int(input("Select carrier (5 spaces) position (0-99): "))
        carrier_orient = str(input("Select carrier orientation (H/V): "))
        self.place_piece(carrier_coord, carrier_orient, 5, )
        # place battleship
        battleship_coord = int(input("Select battleship (4 spaces) position (0-99): "))
        battleship_orient = str(input("Select orientation (H/V): "))
        self.place_piece(battleship_coord, battleship_orient, 4)
        # place submarines
        sub1_coord = int(input("Select submarine (3 spaces) position(0-99): "))
        sub1_orient = str(input("Select orientation (H/V): "))
        self.place_piece(sub1_coord, sub1_orient, 3)
        sub2_coord = int(input("Select second submarine (3 spaces) position(0-99): "))
        sub2_orient = str(input("Select orientation (H/V): "))
        self.place_piece(sub2_coord, sub2_orient, 3)
        sub3_coord = int(input("Select third submarine (3 spaces) position(0-99): "))
        sub3_orient = str(input("Select orientation (H/V): "))
        self.place_piece(sub3_coord, sub3_orient, 3)
        # place cruiser
        cruiser_coord = int(input("Select cruiser (3 spaces) position (0-99): "))
        cruiser_orient = str(input("Select orientation (H/V): "))
        self.place_piece(cruiser_coord, cruiser_orient, 3)
        # place destroyers
        destroyer1_coord = int(input("Select destroyer (2 spaces) position(0-99): "))
        destroyer1_orient = str(input("Select orientation (H/V): "))
        self.place_piece(destroyer1_coord, destroyer1_orient, 2)
        destroyer2_coord = int(input("Select second destroyer (2 spaces) position(0-99): "))
        destroyer2_orient = str(input("Select orientation (H/V): "))
        self.place_piece(destroyer2_coord, destroyer2_orient, 2)
        # place patrol boats
        ptboat1_coord = int(input("Select patrol boat (1 space) position(0-99): "))
        ptboat1_orient = 'H'
        self.place_piece(ptboat1_coord, ptboat1_orient, 1)
        ptboat2_coord = int(input("Select second patrol boat (1 space) position(0-99): "))
        ptboat2_orient = 'H'
        self.place_piece(ptboat2_coord, ptboat2_orient, 1)
        return self.playerBoard

    # method that places a piece on the board
    def place_piece(self, coord, orientation, spaces):
        # create MoveValidator class and pass information to check the moves are okay
        valid = MoveValidator(coord, orientation, spaces, self.playerBoard)
        # check the moves
        valid.check()
        # save the valid moves once they've been checked
        valid_coord = valid.coordinate
        valid_orient = valid.orientation
        self.playerBoard[valid_coord] = '■'
        try:
            if valid_orient == 'H':
                for i in range(1, spaces):
                    self.playerBoard[coord + i] = '■'
            elif valid_orient == 'V':
                for i in range(1, spaces):
                    self.playerBoard[coord + 10 * i] = '■'
        except:
            coord = int(input('The piece you entered fell off the edge. Pick another coordinate: '))
            self.place_piece(coord, valid_orient, spaces)
        self.draw_player_board()

    # method that checks for a win and takes the board as an input
    # returns false if a win does not occur and true if one does
    def check_defeat(self):
        ship_left = False
        for space in self.playerBoard:
            if space == "■":
                ship_left = True
        if ship_left:
            return False
        else:
            print('Oh no! Your last ship has been sunk!')
            print('You lose. Thanks for playing!')
            return True
