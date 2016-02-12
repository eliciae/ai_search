import queue

class SLD_Search:

    def __init__(self):
        return

    def SLD_Search(self, problem, initialState):
        counter = 0
        searchQueue = queue.PriorityQueue()
        searchQueue._put((1,counter,initialState))

        while(not searchQueue.empty()):
            here = searchQueue.get()[2]
            if problem.isGoal(here):
                # print("goal {0}" .format(here.getAStarPath()))
                # print("goal Length {0}" .format(len(here.getAStarPath())-1))
                # print("Actual Cost {0}" .format(here.getActualCost()))
                return here
            else:
                # print("Current Vehicle Location: {0}" .format(here.getVehicleList().getCurrLocation()))
                # print("Actual Path So Far {0}" .format(here.getAStarPath()))
                nextState = problem.successors(here)
                for s in nextState:
                    searchQueue.put((s.getProjectedCost(), counter, s))
                    counter += 1

        return "Failed Hardcore"