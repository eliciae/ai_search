import networkx as nx
import matplotlib.pyplot as plt
import random as rand


class Package:

    def __init__(self, startLocation, endLocation):
        self.source = startLocation
        self.destination = endLocation