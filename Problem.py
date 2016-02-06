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
            star = nx.astar_path(Problem.graph, driver.getCurrLocation(), packageList[0].getNodeStartLocation())
            print(star)
            print("Before Pop: {0}" .format(packageList))
            packagePickedUp = packageList.pop(0)
            print("After Pop: {0}" .format(packageList))
            print("Package Picked up {0}" .format(packagePickedUp))
            if(packageList):
                driver.getPackageList().append(packagePickedUp)
                updatedState = State.State(truck.Vehicle(packagePickedUp.getNodeStartLocation(), driver.getPackageList(), driver.getHomeLocation()), packageList, star)
            else:
                driver.getPackageList().append(packagePickedUp)
                updatedState = State.State(truck.Vehicle(packagePickedUp.getNodeStartLocation(), driver.getPackageList(), driver.getHomeLocation()), packageList, star)

        #if there aren't any packages in the main list
        # but the driver has one on his drop off list
        elif(driver.getPackageList()):
            print("Going to package destination")
            print("End location: {0}" .format(driver.getPackageList()[0].getNodeEndLocation()))
            star = nx.astar_path(Problem.graph, driver.getCurrLocation(), driver.getPackageList()[0].getNodeEndLocation() )
            packageDroppedOff = driver.getPackageList().pop(0)
            if(driver.getPackageList()):
                updatedState = State.State(truck.Vehicle(packageDroppedOff.getNodeEndLocation(), driver.getPackageList(), driver.getHomeLocation()), None, star)
            else:
                updatedState = State.State(truck.Vehicle(packageDroppedOff.getNodeEndLocation(), None, driver.getHomeLocation()), None, star)

        #nothing in either package list or drop off list
        # go home
        elif(not driver.getPackageList()):
            print("Getting the fuck outta here")
            star = nx.astar_path(Problem.graph, driver.getCurrLocation(), driver.getHomeLocation())
            updatedState = State.State(None, None, star)


        return [updatedState]
