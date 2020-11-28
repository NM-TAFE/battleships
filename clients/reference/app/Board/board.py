from clients.reference.app.Board.ShipOrganizer import ShipOrganizer


# Usage, Foreach player, Instantiate 2 board objects,
# 1 x Proper board with the players own ships and status
# 1 x ViewOnly HitTarget board showing misses hits etc

class Board:
    boardLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    horizontalLen = 19

    def __init__(self, _targetingMode=False):
        self.placingPhase = True  # True while board in placing phase
        self.targetingMode = _targetingMode  # For Targeting board view
        self.shipOrgObj = ShipOrganizer()  # Actively modified object of ShipOrgCls
        self.totalShipSquares = 26
        self.board = {
            "A": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # "-----------------------------"
            "B": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # "| |X| | | | |O| | | | | | | |"
            "C": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],  # "-----------------------------"
            "D": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            "E": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            "F": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            "G": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            "H": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            "I": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            "J": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        }

    # TODO: Delete on submission
    def debugBoard(self):
        self.board = {
            "A": ["A", "A", "A", "A", "A", " ", "B", " ", "C", " "],  # "-----------------------------"
            "B": [" ", " ", " ", " ", " ", " ", "B", " ", "C", " "],  # "| |X| | | | |O| | | | | | | |"
            "C": [" ", " ", " ", " ", " ", " ", "B", " ", "C", " "],  # "-----------------------------"
            "D": ["S", "S", "S", " ", "S", " ", "B", " ", " ", " "],
            "E": [" ", " ", " ", " ", "S", " ", " ", " ", " ", "S"],
            "F": [" ", " ", " ", " ", "S", " ", " ", " ", " ", "S"],
            "G": [" ", " ", " ", " ", " ", " ", " ", " ", " ", "S"],
            "H": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            "I": [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            "J": ["P", " ", "D", "D", " ", "D", "D", " ", " ", "P"]
        }

    # def testDefeat(self):
    #     self.total = 1

    def minusShipSquare(self):
        # Take one from ship hits total
        self.totalShipSquares -= 1

    def coordParser(self, _stringCoord):
        # Parse a string cord into a coordinate list

        _tempX, _tempY = _stringCoord

        key_RowLetter = _tempX.upper()  # if not in uppercase, convert it
        value_ColumnIndex = int(_tempY)

        coord_asList = [key_RowLetter, value_ColumnIndex]
        return coord_asList

    def printHorizontalCordNums(self):
        # Print Numbers for top of board
        # No Returns, just print statements
        count = 0
        print(" ", end="")
        for index in range(Board.horizontalLen + 1):
            if (index == 1) | (index % 2 == 1):
                print(f" {count}", end="")
                count += 1

    def printHorizontalLine(self):
        # Print between each line
        # No Returns, just print statements

        print(" ", end="")
        # do we need to print a \n here?
        for i in range(Board.horizontalLen + 2):
            print("-", end="")

    def displayCurrentBoard(self):
        # No Returns, just print statements

        self.printHorizontalCordNums()
        print("\n", end="")
        self.printHorizontalLine()
        for keyparent, valueParent in self.board.items():  # Iterate over each item in dictionary
            # TODO: if this works, remove commented CODE
            # itemCount = 0
            # print(Board.boardLetters[itemCount])
            print(f"\n{keyparent}", end="")
            for value in valueParent:  # Iterate over each value in the itemParent.Value
                print("|", end="")
                print(value, end="")
            print(f"|{keyparent}")  # This may result in broken print at the end
            self.printHorizontalLine()
            # itemCount += 1
        print("\n", end="")
        self.printHorizontalCordNums()
        boardOwner = ""
        if self.targetingMode == True:
            boardOwner = "Opponent's"
        else:
            boardOwner = "Your"
        print("\n" * 2, f"{boardOwner} Board".center(self.horizontalLen + 3, '-'))

        print("\n")

    # TODO: Future implementation may involve isolating these resused code into smaller blocks that are alot more
    #  reusable
    def checkNorth(self, _shipChoice, _rowRef, _rowColRef, _placeMode):
        _shipLength = self.shipOrgObj.getShipLength(_shipChoice)
        for j in range(self.boardLetters.index(_rowRef), (self.boardLetters.index(_rowRef) - _shipLength), -1):
            if (j < 0) or (self.board[self.boardLetters[j]][_rowColRef] != " "):
                return False
            elif (_placeMode):
                self.board[self.boardLetters[j]][_rowColRef] = _shipChoice
        if not _placeMode:
            self.shipOrgObj.addDirection("NORTH")

    def checkEast(self, _shipChoice, _rowRef, _rowColRef, _placeMode):
        _shipLength = self.shipOrgObj.getShipLength(_shipChoice)
        for i in range(_rowColRef, (_rowColRef + _shipLength)):
            if (i > 9) or (self.board[_rowRef][i] != " "):
                return False
            elif _placeMode:
                self.board[_rowRef][i] = _shipChoice
        if not _placeMode:
            self.shipOrgObj.addDirection("EAST")

    def checkSouth(self, _shipChoice, _rowRef, _rowColRef, _placeMode):
        _shipLength = self.shipOrgObj.getShipLength(_shipChoice)
        for i in range(self.boardLetters.index(_rowRef), (self.boardLetters.index(_rowRef) + _shipLength)):
            if (i > 9) or (self.board[self.boardLetters[i]][_rowColRef] != " "):
                return False
            elif _placeMode:
                self.board[self.boardLetters[i]][_rowColRef] = _shipChoice

        if not _placeMode:
            self.shipOrgObj.addDirection("SOUTH")

    def checkWest(self, _shipChoice, _rowRef, _rowColRef, _placeMode):
        _shipLength = self.shipOrgObj.getShipLength(_shipChoice)

        for j in range(_rowColRef, (_rowColRef - _shipLength), -1):
            if (j < 0) or (self.board[_rowRef][j] != " "):
                return False
            elif _placeMode:
                self.board[_rowRef][j] = _shipChoice
        if not _placeMode:
            self.shipOrgObj.addDirection("WEST")

    def checkLegalMoves(self, _shipChoice, _placedPivotPoint):

        _rowRef = _placedPivotPoint[0]
        _rowColRef = _placedPivotPoint[1]
        _placeMode = False

        self.checkNorth(_shipChoice, _rowRef, _rowColRef, _placeMode)
        self.checkEast(_shipChoice, _rowRef, _rowColRef, _placeMode)
        self.checkSouth(_shipChoice, _rowRef, _rowColRef, _placeMode)
        self.checkWest(_shipChoice, _rowRef, _rowColRef, _placeMode)

    # Place Individual Ships
    def placeShip(self, _shipChoice, _placedPivotPoint, _shipDirection):
        _rowRef = _placedPivotPoint[0]
        _rowColRef = _placedPivotPoint[1]
        _placeMode = True

        if _shipDirection == "NORTH":
            self.checkNorth(_shipChoice, _rowRef, _rowColRef, _placeMode)
        elif _shipDirection == "EAST":
            self.checkEast(_shipChoice, _rowRef, _rowColRef, _placeMode)
        elif _shipDirection == "SOUTH":
            self.checkSouth(_shipChoice, _rowRef, _rowColRef, _placeMode)
        elif _shipDirection == "WEST":
            self.checkWest(_shipChoice, _rowRef, _rowColRef, _placeMode)
        elif _shipDirection == "":
            # Must be P - Patrol Boat
            self.markTargetShot(_placedPivotPoint, "P")
        else:
            print("Are you sure you put a correctly spelt direction")

    # MAIN PlacingScript
    def placingShips(self, _debugMode):
        if self.targetingMode:  # simple guard clause
            return

        if _debugMode:
            self.debugBoard()
        else:
            shipsREMAINING = 10
            while shipsREMAINING > 0:
                self.displayCurrentBoard()
                print(self.shipOrgObj.countShipsLeft)
                unplacedShips = self.shipOrgObj.getUnplacedShips()
                for k, v in unplacedShips.items():
                    print(f"{k} - {self.shipOrgObj.translateShipSymbol(k)} has {v} left to place")

                shipChoice = ""  # Hoist empty shipChoice
                while shipChoice not in unplacedShips.keys():
                    shipChoice = input("\nPlease choose one of the above ships to place:").upper()

                checkedPivotPoint = []
                passedCordCheck = False
                while not passedCordCheck:
                    shipPivotPoint = input(f"Please choose a Pivot location for the {shipChoice}\n"
                                           "Example = A3: ")  # A3
                    parsedPivot = self.coordParser(shipPivotPoint)
                    if (parsedPivot[0] in self.boardLetters) and (parsedPivot[1] in range(0, 10)):
                        checkedPivotPoint = parsedPivot
                        passedCordCheck = True
                    else:
                        print("Please choose an appropriate location on board: ")

                self.checkLegalMoves(shipChoice, checkedPivotPoint)
                chooseableDirections = self.shipOrgObj.returnDirections()
                shipDirection = ""
                if shipChoice != "P":
                    while shipDirection not in chooseableDirections:
                        print(f"Legal Directions to place a given "
                              f"\n{self.shipOrgObj.translateShipSymbol(shipChoice)}: ")
                        for i in chooseableDirections:
                            print(f" - {i}")
                        shipDirection = input("Please choose a direction: ").upper()  # WEST, EAST, NORTH, SOUTH

                self.placeShip(shipChoice, checkedPivotPoint, shipDirection)
                self.shipOrgObj.resetDirections()
                self.shipOrgObj.removePlacedShip(shipChoice)
                shipsREMAINING -= 1

        print("All Ships Placed, Sending Ready status to server!")
        self.placingPhase = False

    # Receive And Send Comms
    def receiveShot(self, vectorPoint):
        rowRef, colRef = self.coordParser(vectorPoint)
        if self.board[rowRef][colRef] != " ":
            self.board[rowRef][colRef] = "X"  # Replace Hit square with a destroyed X
            return "HIT"
        else:
            self.board[rowRef][colRef] = "*"
            return "MISS"

    def markTargetShot(self, vectorPoint, symbol):
        rowRef, colRef = self.coordParser(vectorPoint)
        self.board[rowRef][colRef] = f"{symbol}"

    def endCheck(self):
        # if all(value == 0 for value in self.totalShipSquares.values()):
        if self.totalShipSquares == 0:
            return True
        else:
            return False
