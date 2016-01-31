import queue

class Search:

    def __init__(self):
        return

    def search(self, problem, initialState):
        searchQueue = queue.Queue()
        searchQueue.put(initialState)
        while(searchQueue.not_empty):
            here = searchQueue.get()
            if problem.isGoal(here):
                print("goal")
                return here
            else:
                print("called Succesor")
                nextState = problem.successors(here)
                for s in nextState:
                    searchQueue.put(s)
        return "Failed Hardcore"