from ai_search import Vehicle as truck
from ai_search import State2
from ai_search import Package as Pkg
import networkx as nx
import copy


class Problem2:
    graph = None

    def __init__(self, myMap):
        Problem2.graph = myMap

    def isGoal(self, state):
        return not state.getPackageList() and (state.getVehicleList().getCurrLocation() == state.getVehicleList().getHomeLocation())

    def successors(self, state):
        driver = state.getVehicleList()
        packageList = state.getPackageList()
        updatedStateList = []

        if(packageList and driver.getCapacity() > len(driver.getPackageList())):
            for packageIndex in range(0, len(packageList)):
                copyState = copy.deepcopy(state)
                updatedDriver = copyState.getVehicleList()
                packagePickedUp = copyState.getPackageList().pop(packageIndex)
                print("Going to package {0}" .format(packagePickedUp.getNodeStartLocation()))
                updatedDriver.getPackageList().append(packagePickedUp)
                copyState.setProjectedCost(Problem2.pickFarthestPackageAwayPlusDistanceToGarage(self, copyState, packagePickedUp))
                print("Projected Cost: {0}" .format(copyState.getProjectedCost()))
                copyState.setActualCost(Problem2.returnActualCost(self, copyState, packagePickedUp))
                print("Actual Cost: {0}" .format(copyState.getActualCost()))
                copyState.setAStarPath(Problem2.returnAStarPathPickUp(self, state, packagePickedUp))
                copyState.getVehicleList().setCurrLocation(packagePickedUp.getNodeStartLocation())

                updatedStateList.append(copyState)


        # the driver has one or more packages on his drop off list
        if(driver.getPackageList()):
            for driverPackageIndex in range(0, len(driver.getPackageList())):
                copyState = copy.deepcopy(state)
                droppedPackage = copyState.getVehicleList().getPackageList().pop(driverPackageIndex)
                print("Going to package destination")
                copyState.setProjectedCost(Problem2.pickFarthestPackageAwayPlusDistanceToGarage(self,copyState, droppedPackage))
                copyState.setActualCost(Problem2.returnActualCost(self, copyState, droppedPackage))
                copyState.setAStarPath(Problem2.returnAStarPathDropOff(self, state, droppedPackage))
                copyState.getVehicleList().setCurrLocation(droppedPackage.getNodeEndLocation())

                updatedStateList.append(copyState)

        #nothing in either package list or drop off list
        # go home
        if(not driver.getPackageList() and not packageList and not (driver.getCurrLocation() == driver.getHomeLocation())):
            print("Going Home")
            star = nx.astar_path(Problem2.graph, driver.getCurrLocation(), driver.getHomeLocation())
            copyState = copy.deepcopy(state)
            copyState.getVehicleList().setCurrLocation(driver.getHomeLocation())
            copyState.setProjectedCost(len(star))
            #copyState.setActualCost(len(star))
            copyState.setAStarPath(star)
            updatedStateList.append(copyState)


        return updatedStateList


    # Heuristic: the picking up a package (possibly the farthest package) is a good
    # estimate of how much work we need to do.  We want to get the closest estimate
    # we can get to the actual distance --> h(n) <= h*(n) --> optimistic cost <= actual cost
    def pickFarthestPackageAwayPlusDistanceToGarage(self, state, farthestReachablePackage):
        driverHomeLocation = state.getVehicleList().getHomeLocation()
        driverCurrLocation = state.getVehicleList().getCurrLocation()
        #print("Driver's Curr location: {0}" .format(driverCurrLocation))
        packageLocation = farthestReachablePackage.getNodeStartLocation()
        #print("Package's location: {0}" .format(packageLocation))
        driverToPackageDistance = len(nx.astar_path(Problem2.graph, driverCurrLocation, packageLocation))
        packageToHomeDistance = len(nx.astar_path(Problem2.graph, packageLocation, driverHomeLocation))
        projectedDistace = driverToPackageDistance + packageToHomeDistance
        return projectedDistace

    def returnActualCost(self, state, subGoalNode):
        driverCurrLocation = state.getVehicleList().getCurrLocation()
        packageLocation = subGoalNode.getNodeStartLocation()
        print("Actual Path: {0}" .format((nx.astar_path(Problem2.graph, driverCurrLocation, packageLocation))))
        return len(nx.astar_path(Problem2.graph, driverCurrLocation, packageLocation))

    def returnAStarPathPickUp(self, state, subGoalNodePickUp):
        driverCurrLocation = state.getVehicleList().getCurrLocation()
        packageLocation = subGoalNodePickUp.getNodeStartLocation()
        #print("Lenth of A Star: {0}" .format(len(nx.astar_path(Problem2.graph, driverCurrLocation, packageLocation))))
        return nx.astar_path(Problem2.graph, driverCurrLocation, packageLocation)

    def returnAStarPathDropOff(self, state, subGoalNodeDropOff):
        driverCurrLocation = state.getVehicleList().getCurrLocation()
        packageLocation = subGoalNodeDropOff.getNodeEndLocation()
        #print("Lenth of A Star: {0}" .format(len(nx.astar_path(Problem2.graph, driverCurrLocation, packageLocation))))
        return nx.astar_path(Problem2.graph, driverCurrLocation, packageLocation)