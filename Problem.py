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
        vehicles = State.getVehicleList()
        for v in vehicles:
            neighbours = Problem.graph.neighbors(v.getCurrLocation())
            states = list()
            for n in neighbours:
                updatedVehicles = truck.Vehicle()

        # make node into state list from given state
        # returns a node list
        return None
