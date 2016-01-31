class State:
    def __init__(self, vehicleList, packagePickUpList):
        self.vehicleList = vehicleList
        self.packagePickUpList = packagePickUpList

    def getVehicleList(self):
        return self.vehicleList

    def getPackageList(self):
        return self.packagePickUpList
