class Vehicle:
    def __init__(self, myHomeLocation):
        self.myLoadOfPackages = []
        self.myHomeLocation = myHomeLocation
        self.myCurrentLocation = self.myHomeLocation

    def getCurrLocation(self):
        return self.myCurrentLocation

    def getHomeLocation(self):
        return self.myHomeLocation
    