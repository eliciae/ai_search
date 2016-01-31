from ai_search import Vehicle as truck

class Problem:

    def __init__(self, map, listOfPackages, listOfVehicles):
        self.map = map
        self.listOfPackages = listOfPackages
        self.listOfVehicles = listOfVehicles

    def isGoal(self, state):
        return not self.listOfPackages and not self.listOfVehicles


    def successors(self, state):
        return None
