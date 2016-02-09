class Vehicle:
    def __init__(self, myCurrLocation, myPackageList, myHomeLocation, capacity):
        self.myPackageList = myPackageList
        self.myCurrentLocation = myCurrLocation
        self.myHomeLocation = myHomeLocation
        self.capacity = capacity

    def getCurrLocation(self):
        return self.myCurrentLocation

    def setCurrLocation(self, currLocation):
        self.myCurrentLocation = currLocation

    def getPackageList(self):
        return self.myPackageList

    def setPackageList(self, packageList):
        self.myPackageList = packageList

    def getHomeLocation(self):
        return self.myHomeLocation

    def getCapacity(self):
        return self.capacity