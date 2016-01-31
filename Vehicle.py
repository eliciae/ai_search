class Vehicle:
    def __init__(self, myCurrLocation, myPackageList, myHomeLocation):
        self.myPackageList = myPackageList
        self.myCurrentLocation = myCurrLocation
        self.myHomeLocation = myHomeLocation

    def getCurrLocation(self):
        return self.myCurrentLocation

    def setCurrLocation(self, currLocation):
        self.myCurrentLocation = currLocation

    def getPackageList(self):
        return self.myPackageList

    def setPackageList(self, packageList):
        self.myPackageList = packageList

    def getMyHomeLocation(self):
        return self.myHomeLocation