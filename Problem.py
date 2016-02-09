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
                star = nx.astar_path(Problem.graph, updatedDriver.getCurrLocation(), packagePickedUp.getNodeStartLocation())
                print(star)
                updatedDriver.getPackageList().append(packagePickedUp)
                # print("Before Original Package List {0}" .format(state.getPackageList()))
                # print("Before Copy List {0}" .format(copyState.getPackageList))
                #
                #
                # print("After Original Package List {0}" .format(state.getPackageList()))
                # print("After Copy List {0}" .format(copyState.getPackageList))
                copyState.setAStarList(star)
                copyState.getVehicleList().setCurrLocation(packagePickedUp.getNodeStartLocation())
                updatedStateList.append(copyState)


        #if there aren't any packages in the main list
        # but the driver has one on his drop off list
        if(driver.getPackageList()):
            for driverPackageIndex in range(0, len(driver.getPackageList())):
                copyState = copy.deepcopy(state)
                droppedPackage =  copyState.getVehicleList().getPackageList().pop(driverPackageIndex)
                print("Going to package destination")
                print("End location: {0}" .format(droppedPackage.getNodeEndLocation()))
                star = nx.astar_path(Problem.graph, driver.getCurrLocation(), droppedPackage.getNodeEndLocation() )
                print(star)
                copyState.setAStarList(star)
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
