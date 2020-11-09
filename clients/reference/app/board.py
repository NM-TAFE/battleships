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

    def record_strike(self):
        if self.playerBoard == "0":
            return "miss"
        if self.playerBoard == "S":
            return "hit"

    def place_ships(self):
        aircraft_carrier = int(input("Select aircraft carrier position(0-99): "))
        battlship = int(input("Select battleship Position: "))
        submarine1 = int(input("Select submarine position(0-99): "))
        submarine2 = int(input("Select second submarine position(0-99): "))
        submarine3 = int(input("Select third submarine position(0-99): "))
        cruiser = int(input("Select cruiser position (0-99): "))
        destroyer1 = int(input("Select destroyer position(0-99): "))
        destroyer2 = int(input("Select second destroyer position(0-99): "))
        ptboat1 = int(input("Select patrol boat position(0-99): "))
        ptboat2 = int(input("Select second patrol boat position(0-99): "))