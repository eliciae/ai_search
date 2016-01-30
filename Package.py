import networkx as nx
import matplotlib.pyplot as plt
import random as rand


class Package:
    def __init__(self, startLocation, endLocation):
        self.startLocation = startLocation
        self.endLocation = endLocation

    def getNodeStartLocation(self):
        return self.startLocation

    def getNodeEndLocation(self):
        return self.endLocation
