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
        updatedStateList = []
        # print("Driver package list {0}" .format(driver.getPackageList()))
        ##side comment: if there are multiple drivers

        #if there is still a package in the main package
        #list
        if(packageList):

            for p in packageList:
                print("Going to package")
                star = nx.astar_path(Problem.graph, driver.getCurrLocation(), p.getNodeStartLocation())
                print(star)
                #print("Before Pop: {0}" .format(packageList))
                packagePickedUp = p
                # print("After Pop: {0}" .format(packageList))
                # print("Package Picked up {0}" .format(packagePickedUp))
                driver.getPackageList().append(packagePickedUp)
                packageList.remove(p)
                updatedState = State.State(truck.Vehicle(packagePickedUp.getNodeStartLocation(), driver.getPackageList(), driver.getHomeLocation()), packageList, star)
                updatedStateList.append(updatedState)

        #if there aren't any packages in the main list
        # but the driver has one on his drop off list
        if(driver.getPackageList):
            for dPackage in driver.getPackageList():
                print("Going to package destination")
                print("End location: {0}" .format(dPackage.getNodeEndLocation()))
                star = nx.astar_path(Problem.graph, driver.getCurrLocation(), dPackage.getNodeEndLocation() )
                print(star)
                packageDroppedOff = dPackage
                driver.getPackageList().remove(dPackage)
                updatedState = State.State(truck.Vehicle(packageDroppedOff.getNodeEndLocation(), driver.getPackageList(), driver.getHomeLocation()), packageList, star)
                updatedStateList.append(updatedState)

        #nothing in either package list or drop off list
        # go home
        if(not driver.getPackageList() and not packageList):
            print("Getting the fuck outta here")
            star = nx.astar_path(Problem.graph, driver.getCurrLocation(), driver.getHomeLocation())
            print(star)
            updatedState = State.State(None, None, star)
            updatedStateList.append(updatedState)


        return updatedStateList
