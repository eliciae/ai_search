class State:
    def __init__(self, vehicleList, packagePickUpList, heuristicValue):
        self.vehicleList = vehicleList
        self.packagePickUpList = packagePickUpList
        self.heuristicValue = heuristicValue

    def getVehicleList(self):
        return self.vehicleList

    def getPackageList(self):
        return self.packagePickUpList

    def getHeuristicValue(self):
        return self.heuristicValue

    def setHeuristicValue(self, hVal):
        self.heuristicValue = hVal
