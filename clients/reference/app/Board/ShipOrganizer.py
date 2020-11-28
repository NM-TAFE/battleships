class ShipOrganizer(object):

    def __init__(self):
        # Consts
        self.shipLengthConsts = {"A": 5, "B": 4, "S": 3, "C": 3, "D": 2, "P": 1}
        # A = Aircraft Carrier
        # B = Battleship
        # S = Submarine
        # C = Light Cruiser
        # D = Destroyer
        # P = Patrol Boat
        self.shipTranslate = {"A": "Aircraft-Carrier", "B": "Battleship", "S": "Submarine", "C": "Cruiser",
                              "D": "Destroyer", "P": "Patrol Boat"}

        # Instance Changing Variables
        self.countShipsLeft = 10
        self.shipsLeft = {"A": 1, "B": 1, "S": 3, "C": 1, "D": 2, "P": 2}
        self.tempDirectionStore = []

    def addDirection(self, _direction):
        self.tempDirectionStore.append(_direction)

    def returnDirections(self):
        return self.tempDirectionStore

    def resetDirections(self):
        self.tempDirectionStore = []

    def shipsToPlaceCount(self):
        valuesList = self.shipsLeft.values()
        sumValues = sum(valuesList)
        self.countShipsLeft = sumValues

    def removePlacedShip(self, ship):
        self.shipsLeft[ship] -= 1  # TODO: This may not work

    def getUnplacedShips(self):
        unplacedShips = {}
        for k, v in self.shipsLeft.items():
            if v != 0:
                unplacedShips.update({k: v})
        return unplacedShips

    def translateShipSymbol(self, _ship):
        return self.shipTranslate[_ship]

    def getShipLength(self, ship):
        _shipLength = self.shipLengthConsts[ship]
        return _shipLength
