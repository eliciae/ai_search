class Vehicle:
    def __init__(self, myCurrLocation, myPackageList):
        self.myLoadOfPackages = myPackageList
        self.myCurrentLocation = myCurrLocation

    def getCurrLocation(self):
        return self.myCurrentLocation

    def setCurrLocation(self, currLocation):
        self.myHomeLocation = currLocation

    def getPackageList(self):
        return self.getPackageList()

    def setPackageList(self, packageList):
        self.myLoadOfPackages = packageList