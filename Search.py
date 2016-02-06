import queue

class Search:

    def __init__(self):
        return

    def search(self, problem, initialState):
        searchQueue = queue.PriorityQueue()
        searchQueue.put(initialState)
        while(searchQueue.not_empty):
            here = searchQueue.get()
            if problem.isGoal(here):
                print("goal")
                return here
            else:
                print("Current Vehicle Location: {0}" .format(here.getVehicleList().getCurrLocation()))
                nextState = problem.successors(here)
                for s in nextState:
                    searchQueue.put(len(s.getAStarList()), s)
                #print(nextState.getVehicleList().getCurrLocation())
        return "Failed Hardcore"