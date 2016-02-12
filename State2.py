class State2:
    def __init__(self, vehicleList, packagePickUpList, projectedCost, actualCost):
        self.vehicleList = vehicleList
        self.packagePickUpList = packagePickUpList
        self.actualCost = actualCost
        self.projectedCost = projectedCost
        self.CurrentAStarPath = []

    def getVehicleList(self):
        return self.vehicleList

    def getPackageList(self):
        return self.packagePickUpList

    # the projected cost of a "potential move"
    # currently our potential move is defined as
    # the the number of moves(distance) to drop off
    # a package and go home
    # OR
    # the number of moves to pick up a package
    # and go home
    def getProjectedCost(self):
        return self.projectedCost

    def setProjectedCost(self, projectedCost):
        self.projectedCost = projectedCost

    # The actual cost of the trip so far..
    # undecided if this will be used as the
    # actual cost of the transition or the total
    # cost of the whole trip
    def getActualCost(self):
        return self.actualCost

    def setActualCost(self, actualCost):
        self.actualCost += actualCost

    # Get the A* path
    def getAStarPath(self):
        return self.CurrentAStarPath

    # Make the list of path the carrier travels
    # to make it to the goal
    def setAStarPath(self, star):
        print("Current Path: {0},  Path Added: {1}" .format(len(self.CurrentAStarPath), len(star)))
        self.CurrentAStarPath += star
