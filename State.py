class State:
    def __init__(self, myVehicle, myListOfPackages):
        self.MyVehicle = myVehicle
        self.MyListOfPackages = myListOfPackages

    def getMyVehicle(self):
        return self.MyVehicle

    def getMyPackageList(self):
        return self.MyListOfPackages
