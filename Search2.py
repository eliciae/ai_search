import queue
from ai_search import StateQueue
from ai_search import State2

class Search2:

    def __init__(self):
        return

    def search2(self, problem, initialState):

        searchQueue = StateQueue.StateQueue()
        searchQueue.add(initialState)

        while(not searchQueue.isEmpty()):
            here = searchQueue.pop()
            if problem.isGoal(here):
                print("goal {0}" .format(here.getAStarPath()))
                print("Actual Cost {0}" .format(here.getActualCost()))
                return here
            else:
                print("Current Vehicle Location: {0}" .format(here.getVehicleList().getCurrLocation()))
                nextState = problem.successors(here)
                for s in nextState:
                    searchQueue.add(s)

        return "Failed Hardcore"