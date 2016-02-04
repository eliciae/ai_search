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
        package = state.getPackageList()
        updatedState = None
        ##side comment: if there are multiple drivers

        #if there is still a package in the main package
        #list
        if(package):
            print("Going to package")
            print(nx.astar_path(Problem.graph, driver.getCurrLocation(), package.getNodeStartLocation()))
            updatedState = State.State(truck.Vehicle(package.getNodeStartLocation(), package, driver.getHomeLocation()), None)

        #if there aren't any packages in the main list
        # but the driver has one on his drop off list
        elif(not package and driver.getPackageList()):
            print("Going to package destination")
            print(nx.astar_path(Problem.graph, driver.getCurrLocation(), driver.getPackageList().getNodeEndLocation() ))
            updatedState = State.State(truck.Vehicle(driver.getPackageList().getNodeEndLocation(), None, driver.getHomeLocation()), None)

        #nothing in either package list or drop off list
        # go home
        elif(not package and not driver.getPackageList()):
            print("Getting the fuck outta here")
            print(nx.astar_path(Problem.graph, driver.getCurrLocation(), driver.getHomeLocation()))
            updatedState = State.State(None, None)


        return [updatedState]
