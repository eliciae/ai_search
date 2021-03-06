import queue

class Search:

    def __init__(self):
        return

    def search(self, problem, initialState):
        counter = 0
        searchQueue = queue.PriorityQueue()

        searchQueue.put((1, counter, initialState))

        while(searchQueue.not_empty):
            here = searchQueue.get()
            searchQueue = queue.PriorityQueue()
            # variable "here" is a tuple. here[2] access the state
            state = here[2]
            if problem.isGoal(state):
                print("goal")
                return here
            else:
                nextState = problem.successors(state)
                print("Current Vehicle Location: {0}" .format(state.getVehicleList().getCurrLocation()))
                print("Current Vehicle PackageList: {0}" .format(state.getVehicleList().getPackageList()))
                for s in nextState:
                    counter = counter + 1
                    searchQueue.put((s.getHeuristicValue(), counter, s))
                #print(nextState.getVehicleList().getCurrLocation())
        return "Failed Hardcore"