from ai_search import Vehicle as truck
from ai_search import State
from ai_search import Package as Pkg
import networkx as nx


class Problem:
    graph = None

    def __init__(self, myMap):
        Problem.graph = myMap
        #self.listOfPackages = listOfPackages
        #self.listOfVehicles = listOfVehicles

    def isGoal(self, state):
        return not state.getPackageList() and not state.getVehicleList()

    def successors(self, state):
        # getNeighbours(current Node) curr node comes from the
        # vehicle which comes from a state
        states = []
        vehicle = state.getVehicleList()
        package = state.getPackageList()
        neighbours = Problem.graph.neighbors(vehicle.getCurrLocation())
        for n in neighbours:
            if package:
                updatedPackageList = Pkg.Package(package.getNodeStartLocation(), package.getNodeEndLocation())
            else:
                updatedPackageList = None
            updatedVehicleList = truck.Vehicle(n, updatedPackageList, vehicle.getMyHomeLocation())
            updatedVehicleList.setCurrLocation(n)
            # drop off
            if updatedVehicleList.getPackageList() and n == updatedVehicleList.getPackageList().getNodeEndLocation():
                updatedVehicleList.setPackageList(None)
            # pick up
            if package and n == package.getNodeStartLocation():
                updatedVehicleList.setPackageList(package)
                updatedPackageList = None
            # vehicle home and no more packages
            if (state.getPackageList() == None and vehicle.getPackageList() == None) and n == vehicle.getMyHomeLocation():
                updatedVehicleList = None
            states.append(State.State(updatedVehicleList, updatedPackageList))
        return states


        # states = []
        # vehicles = State.getVehicleList()
        # for v in vehicles:
        #     possibleVehicles = []
        #     updatedPickupList = state.getPackageList()
        #     neighbours = Problem.graph.neighbors(v.getCurrLocation())
        #     for n in neighbours:
        #         # pass along the package list belonging to the truck
        #         truckPackages = v.getPackageList()
        #         # if n is the destination of a package they are carrying, drop it off
        #         for pkg in truckPackages:
        #             if pkg.getEndLocation() == n:
        #                 truckPackages.remove(pkg)
        #         # if n has a package, pick it up
        #         for pkg in state.getPackageList():
        #             if pkg.getStartLocation() == n:
        #                 truckPackages.append(pkg)
        #                 updatedPickupList.remove(pkg)
        #         possibleVehicles.append(truck.Vehicle(n, truckPackages))
        #         for pv in possibleVehicles:
        #             states.append(State(list(pv), updatedPickupList))




        # make node into state list from given state
        # returns a node list
        return None
