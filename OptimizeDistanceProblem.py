import networkx as nx
import copy

class OptimizeDistanceHeuristic:
    graph = None


    def __init__(self, myMap, function):
        OptimizeDistanceHeuristic.graph = myMap
        self.heuristicFunction = function()

    def isGoal(self, state):
        return (state.getPackageList()==[]) and (state.getVehicleList().getCurrLocation() == state.getVehicleList().getHomeLocation()) and (state.getVehicleList().getPackageList()==[])

    def successors(self, state):
        driver = state.getVehicleList()
        packageList = state.getPackageList()
        updatedStateList = []


        if(packageList and driver.getCapacity() > len(driver.getPackageList())):
            for packageIndex in range(0, len(packageList)):
                copyState = copy.deepcopy(state)
                updatedDriver = copyState.getVehicleList()
                packagePickedUp = copyState.getPackageList().pop(packageIndex)
                #print("Going to package {0}" .format(packagePickedUp.getNodeStartLocation()))
                updatedDriver.getPackageList().append(packagePickedUp)
                copyState.setProjectedCost(self.heuristicFunction(self, copyState, packagePickedUp))
                #print("Projected Cost: {0}" .format(copyState.getProjectedCost()))
                copyState.setActualCost(OptimizeDistanceHeuristic.returnActualCostPickUp(self, copyState, packagePickedUp))
                #print("Actual Cost: {0}" .format(copyState.getActualCost()))
                copyState.setAStarPath(OptimizeDistanceHeuristic.returnAStarPathPickUp(self, copyState, packagePickedUp))
                copyState.getVehicleList().setCurrLocation(packagePickedUp.getNodeStartLocation())
                print("State Created")
                updatedStateList.append(copyState)


        # the driver has one or more packages on his drop off list
        if(driver.getPackageList()):
            for driverPackageIndex in range(0, len(driver.getPackageList())):
                copyState = copy.deepcopy(state)
                droppedPackage = copyState.getVehicleList().getPackageList().pop(driverPackageIndex)
                print("Going to package destination")
                copyState.setProjectedCost(self.heuristicFunction(self, copyState, droppedPackage))
                copyState.setActualCost(OptimizeDistanceHeuristic.returnActualCostDropOff(self, copyState, droppedPackage))
                copyState.setAStarPath(OptimizeDistanceHeuristic.returnAStarPathDropOff(self, copyState, droppedPackage))
                copyState.getVehicleList().setCurrLocation(droppedPackage.getNodeEndLocation())
                print("Driver State Created")
                updatedStateList.append(copyState)

        #nothing in either package list or drop off list
        # go home
        if(not driver.getPackageList() and not packageList and not (driver.getCurrLocation() == driver.getHomeLocation())):
            print("Going Home")
            star = nx.astar_path(OptimizeDistanceHeuristic.graph, driver.getCurrLocation(), driver.getHomeLocation())
            copyState = copy.deepcopy(state)
            copyState.getVehicleList().setCurrLocation(driver.getHomeLocation())
            copyState.setProjectedCost(len(star))
            #copyState.setActualCost(len(star))
            copyState.setAStarPath(star)
            copyState.setActualCost(len(star))
            updatedStateList.append(copyState)
            print("Final State Created")


        return updatedStateList

    def returnActualCostPickUp(self, state, subGoalNode):
        driverCurrLocation = state.getVehicleList().getCurrLocation()
        packageLocation = subGoalNode.getNodeStartLocation()
        #print("Actual Path: {0}" .format((nx.astar_path(Problem2.graph, driverCurrLocation, packageLocation))))
        return (len(nx.astar_path(OptimizeDistanceHeuristic.graph, driverCurrLocation, packageLocation))-1)

    def returnActualCostDropOff(self, state, subGoalNode):
        driverCurrLocation = state.getVehicleList().getCurrLocation()
        packageLocation = subGoalNode.getNodeEndLocation()
        #print("Actual Path: {0}" .format((nx.astar_path(Problem2.graph, driverCurrLocation, packageLocation))))
        return (len(nx.astar_path(OptimizeDistanceHeuristic.graph, driverCurrLocation, packageLocation))-1)

    def returnAStarPathPickUp(self, state, subGoalNodePickUp):
        driverCurrLocation = state.getVehicleList().getCurrLocation()
        packageLocation = subGoalNodePickUp.getNodeStartLocation()
        #print("Lenth of A Star: {0}" .format(len(nx.astar_path(Problem2.graph, driverCurrLocation, packageLocation))))
        return nx.astar_path(OptimizeDistanceHeuristic.graph, driverCurrLocation, packageLocation)

    def returnAStarPathDropOff(self, state, subGoalNodeDropOff):
        driverCurrLocation = state.getVehicleList().getCurrLocation()
        packageLocation = subGoalNodeDropOff.getNodeEndLocation()
        #print("Lenth of A Star: {0}" .format(len(nx.astar_path(Problem2.graph, driverCurrLocation, packageLocation))))
        return nx.astar_path(OptimizeDistanceHeuristic.graph, driverCurrLocation, packageLocation)