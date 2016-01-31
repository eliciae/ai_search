from ai_search import Vehicle as truck
from ai_search import State
import networkx as nx


class Problem:
    graph = None

    def __init__(self, myMap, listOfPackages, listOfVehicles):
        Problem.graph = myMap
        self.listOfPackages = listOfPackages
        self.listOfVehicles = listOfVehicles

    def isGoal(self, state):
        return not self.listOfPackages and not self.listOfVehicles

    def successors(self, state):
        # getNeighbours(current Node) curr node comes from the
        # vehicle which comes from a state
        states = []
        vehicles = State.getVehicleList()
        for v in vehicles:
            possibleVehicles = []
            updatedPickupList = state.getPackageList()
            neighbours = Problem.graph.neighbors(v.getCurrLocation())
            for n in neighbours:
                # pass along the package list belonging to the truck
                truckPackages = v.getPackageList()
                # if n is the destination of a package they are carrying, drop it off
                for pkg in truckPackages:
                    if pkg.getEndLocation() == n:
                        truckPackages.remove(pkg)
                # if n has a package, pick it up
                for pkg in state.getPackageList():
                    if pkg.getStartLocation() == n:
                        truckPackages.append(pkg)
                        updatedPickupList.remove(pkg)
                possibleVehicles.append(truck.Vehicle(n, truckPackages))
                for pv in possibleVehicles:
                    states.append(State(list(pv), updatedPickupList))



        # make node into state list from given state
        # returns a node list
        return None
