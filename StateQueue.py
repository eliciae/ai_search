from ai_search import State2

class StateQueue:

    def __init__(self):
        self.potentialStates = []

    def pop(self):
        return self.potentialStates.pop()

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