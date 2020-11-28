"""
ship class holds the entire server's players of ships
"""
class Ships():
    def __init__(self):
        #key to hold all ships in a game
        # multiple versions of ships needs different key to ensure a ship will be destroyed.
        defaultKey = (
                ["A"] * 5 +
                ["B"] * 4 +
                ["S1"] * 3 +
                ["S2"] * 3 +
                ["S3"] * 3 +
                ["C"] * 3 +
                ["D1"] * 2 +
                ["D2"] * 2 +
                ["P1"] * 2 +
                ["P2"] * 2
        )
        #dictionary to hold the names of the ships based on the target code for each ship
        name = {"A": "Aircraft Carrier",
                "B": "Battleship",
                "S1": "Submarine",
                "S2": "Submarine",
                "S3": "Submarine",
                "C": "Cruiser",
                "D1": "Destroyer",
                "D2": "Destroyer",
                "P1": "Patrol Boat",
                "P2": "Patrol Boat"
                }
        #dict for the server's storage of ships
        #format is userId:defaultKey
        data = {}
    #sets the new user id into the data with new set of ships
    def prepareShips(self, myId):
        #validator to ensure str is being passed
        if type(myId) is not str:
            myId = str(myId)
        self.data[myId] = self.defaultKey[:]

    #removes the ship key from the list once it has been hit
    def attackShip(self, myId, target):
        if type(myId) is not str:
            myId = str(myId)
        attackList = self.data[myId]
        hitMsg = "You have hit a ship."
        attackList.remove(str(target))

    #will check if all iterations of the ship has been removed and return msg
    #won't return any str if all iterations aren't gone
    def checkSunk(self,myId, target):
        msg = "\nYou have sunk my "
        if type(myId) is not str:
            myId = str(myId)
        if target not in self.data[myId]:
            destroyed = self.name[str(target)]
            msg = msg + destroyed + '.'
            return msg



