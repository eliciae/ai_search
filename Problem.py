from ai_search import Vehicle as truck
from ai_search import State
from ai_search import Package as Pkg
import networkx as nx
import copy


class Problem:
    graph = None

    def __init__(self, myMap):
        Problem.graph = myMap

    def isGoal(self, state):
        return not state.getPackageList() and not state.getVehicleList() and (state.getVehicleList().getCurrLocation() == state.getVehicleList().getHomeLocation())

    def successors(self, state):
        driver = state.getVehicleList()
        packageList = state.getPackageList()
        updatedStateList = []
        # print("Driver package list {0}" .format(driver.getPackageList()))
        ##side comment: if there are multiple drivers

        #if there is still a package in the main package
        #list
        # and the driver has room to pick it up
        if(packageList and driver.getCapacity() > len(driver.getPackageList())):
            for packageIndex in range(0, len(packageList)):
                copyState = copy.deepcopy(state)
                updatedDriver = copyState.getVehicleList()
                packagePickedUp = copyState.getPackageList().pop(packageIndex)
                print("Going to package")
                updatedDriver.getPackageList().append(packagePickedUp)
                # print("Before Original Package List {0}" .format(state.getPackageList()))
                # print("Before Copy List {0}" .format(copyState.getPackageList))
                #
                #
                # print("After Original Package List {0}" .format(state.getPackageList()))
                # print("After Copy List {0}" .format(copyState.getPackageList))
                copyState.setHeuristicValue(heuristic(False, packagePickedUp, copyState))
                copyState.getVehicleList().setCurrLocation(packagePickedUp.getNodeStartLocation())
                updatedStateList.append(copyState)


        # the driver has one or more packages on his drop off list
        if(driver.getPackageList()):
            for driverPackageIndex in range(0, len(driver.getPackageList())):
                copyState = copy.deepcopy(state)
                droppedPackage =  copyState.getVehicleList().getPackageList().pop(driverPackageIndex)
                print("Going to package destination")
                print("End location: {0}" .format(droppedPackage.getNodeEndLocation()))
                copyState.setHeuristicValue(heuristic(True, droppedPackage, copyState))
                copyState.getVehicleList().setCurrLocation(droppedPackage.getNodeEndLocation())
                updatedStateList.append(copyState)

        #nothing in either package list or drop off list
        # go home
        if(not driver.getPackageList() and not packageList and (driver.getCurrLocation() != driver.getHomeLocation())):
            print("Getting the fuck outta here")
            star = nx.astar_path(Problem.graph, driver.getCurrLocation(), driver.getHomeLocation())
            print(star)
            driver.setCurrLocation(driver.getHomeLocation())
            updatedState = State.State(driver, None, star)
            updatedStateList.append(updatedState)


        return updatedStateList


# take into account the number of packages you have and the distance to the nearest drop/pickup
# node, giving higher preference to the drop nodes when you are closer to capacity
# --- combine these two ideas ---
# if the num packages left is greater than the number remaining/num cars
# then go drop things off and let the other cars deal with it
def heuristic(isDropNode, package, state):
    driver = state.getVehicleList()
    #a backwards array of the capacity to award points
    points = [i for i in range(0, driver.getCapacity())]
    points.reverse()
    #drop off
    if isDropNode:
        star = len(nx.astar_path(Problem.graph, driver.getCurrLocation(), package.getNodeEndLocation()))
        # don't penalize for dropping off
        totalVal = star
    #pick up
    else:
        star = len(nx.astar_path(Problem.graph, driver.getCurrLocation(), package.getNodeStartLocation()))
        # the lower the difference between capacity and num packages you have, the greater the penalty
        totalVal = star + points[(driver.getCapacity() - len(driver.getPackageList()))]

    return totalVal

# def heuristic1(isDropNode, package, state):
#     driver = state.getVehicleList()
#     #drop off
#     if isDropNode:
#         star = len(nx.astar_path(Problem.graph, driver.getCurrLocation(), package.getNodeEndLocation()))
#
#     #pick up
#     else:
#         star = len(nx.astar_path(Problem.graph, driver.getCurrLocation(), package.getNodeStartLocation()))
#
#     return totalVal