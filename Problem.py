from ai_search import Vehicle as truck
from ai_search import State
from ai_search import Package as Pkg
import networkx as nx


class Problem:
    graph = None

    def __init__(self, myMap):
        Problem.graph = myMap

    def isGoal(self, state):
        return not state.getPackageList() and not state.getVehicleList()

    def successors(self, state):
        driver = state.getVehicleList()
        packageList = state.getPackageList()
        print("Driver package list {0}" .format(driver.getPackageList()))
        ##side comment: if there are multiple drivers

        #if there is still a package in the main package
        #list
        if(packageList):
            print("Going to package")
            print(nx.astar_path(Problem.graph, driver.getCurrLocation(), packageList[0].getNodeStartLocation()))
            print("Before Pop: {0}" .format(packageList))
            packagePickedUp = packageList.pop(0)
            print("After Pop: {0}" .format(packageList))
            print("Package Picked up {0}" .format(packagePickedUp))
            if(packageList):
                driver.getPackageList().append(packageList[0])
                updatedState = State.State(truck.Vehicle(packageList[0].getNodeStartLocation(), driver.getPackageList(), driver.getHomeLocation()), packageList)
            else:
                driver.getPackageList().append(packagePickedUp)
                updatedState = State.State(truck.Vehicle(packagePickedUp.getNodeStartLocation(), driver.getPackageList(), driver.getHomeLocation()), packageList)

        #if there aren't any packages in the main list
        # but the driver has one on his drop off list
        elif(driver.getPackageList()):
            print("Going to package destination")
            print(nx.astar_path(Problem.graph, driver.getCurrLocation(), driver.getPackageList()[0].getNodeEndLocation() ))
            driver.getPackageList().pop(0)
            if(driver.getPackageList()):
                updatedState = State.State(truck.Vehicle(driver.getPackageList()[0].getNodeEndLocation(), driver.getPackageList(), driver.getHomeLocation()), None)
            else:
                updatedState = State.State(truck.Vehicle(driver.getPackageList()[0].getNodeEndLocation(), driver.getPackageList(), driver.getHomeLocation()), None)

        #nothing in either package list or drop off list
        # go home
        elif(not driver.getPackageList()):
            print("Getting the fuck outta here")
            print(nx.astar_path(Problem.graph, driver.getCurrLocation(), driver.getHomeLocation()))
            updatedState = State.State(None, None)


        return [updatedState]
