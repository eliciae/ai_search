class State:
    def __init__(self, vehicleList, packagePickUpList, aStarList):
        self.vehicleList = vehicleList
        self.packagePickUpList = packagePickUpList
        self.aStarList = aStarList

    def getVehicleList(self):
        return self.vehicleList

    def getPackageList(self):
        return self.packagePickUpList

    def getAStarList(self):
        return self.aStarList

    def setAStarList(self, aStarList):
        self.aStarList = aStarList
