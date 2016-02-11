from ai_search import State2

class StateQueue:

    def __init__(self):
        self.potentialStates = []

    # The way the StateQueue.add(state) is working is adding the
    # shortest path to the front but we want to explore the longest
    # path since its a good estimate of the work we have to do
    def pop(self):
        return self.potentialStates.pop(len(self.potentialStates)-1)

    #NEED TO FIX THE INSERT.....
    def add(self, state):
        if(self.potentialStates == []):
            self.potentialStates.append(state)
        else:
            # insert(position, item)
            position = (state.getProjectedCost() + state.getActualCost())
            self.potentialStates.insert(position, state)

    def size(self):
        return len(self.potentialStates)

    def isEmpty(self):
        return self.potentialStates == []