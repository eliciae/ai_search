
import networkx as nx
import matplotlib.pyplot as plt
import random as rand
from ai_search import Package as pkg
from ai_search import Problem as prob
from ai_search import Vehicle as truck
from ai_search import State
from ai_search import Search


def makeMap(m, n, gapfreq):
    """ Creates a graph in the form of a grid, with mXn nodes.
    The graph has irregular holes poked into it by random deletion.

    :param m: number of nodes on one dimension of the grid
    :param n: number of nodes on the other dimension
    :param gapfreq: the fraction of nodes to delete (see function prune() below)
    :return: a networkx graph with nodes and edges.

    The default edge weight is  (see below).  The edge weights can be changed by
    designing a list that tells the frequency of weights desired.
      100% edge weights 1:  [(1,100)]
      50% weight 1; 50% weight 2: [(1,50),(2,100)]
      33% each of 1,2,5: [(1,33),(2,67),(5,100)]
      a fancy distribution:  [(1,10),(4,50),(6,90),(10,100)]
      (10% @ 1, 40% @ 4, 40% @ 6, 10% @ 10)
    """
    g = nx.grid_2d_graph(m, n)
    weights = [(1, 100)]
    prune(g, gapfreq)
    setWeights(g, weights)
    return g


def setWeights(g, weights):
    """ Use the weights list to set weights of graph g
    :param g: a networkx graph
    :param weights: a list of pairs [(w,cf) ... ]
    :return: nothing

    weights are [(w,cf) ... ]
    w is the weight, cf is the cumulative frequency

    This function uses a uniform random number to index into the weights list.
    """
    for (i, j) in nx.edges(g):
        c = rand.randint(1,100)
        w = [a for (a,b) in weights if b >= c] # drop all pairs whose cf is < c
        g.edge[i][j]['weight'] = w[0]  # take the first weight in w
    return


def draw(g):
    """ Draw the graph, just for visualization.  Also creates a jpg in $CWD
    :param g: a networkx graph
    :return:
    """
    pos = {n: n for n in nx.nodes(g)}
    nx.draw_networkx_nodes(g, pos, node_size=20)
    edges = nx.edges(g)
    nx.draw_networkx_edges(g, pos, edgelist=edges, width=1)
    plt.axis('off')
    plt.savefig("simplegrid.png")  # save as png
    plt.show()  # display
    return


def prune(g, gapf):
    """ Poke random holes the graph g by deleting random nodes, with probability gapf.
    Then clean up by deleting all but the largest connected component.

    Interesting range (roughly):  0.1 < gapf < 0.3
    values too far above 0.3 lead to lots of pruning, but rather smaller graphs

    :param g: a networkx graph
    :param gapf: a fraction in [0,1]
    :return: nothing
    """
    # creating gaps...
    for node in nx.nodes(g):
        if rand.random() < gapf:
            g.remove_node(node)
    # deleting all but the largest connected component...
    comps = sorted(nx.connected_components(g), key=len, reverse=False)
    while len(comps) > 1:
        nodes = comps[0]
        for node in nodes:
            g.remove_node(node)
        comps.pop(0)


def addPackages(g, numPkg):
    """
    creates a list of packages that are assigned an integer id based on where they are placed in the graph

    :param g: networkx graph
    :param numPkg: the number of packages that should be randomly added to the graph
    :return: a list of packages
    """
    pkgList = []
    for i in range(0, numPkg):
        pkgList.append(pkg.Package(rand.choice(g.nodes()), rand.choice(g.nodes())))
    return pkgList

# script to use the above functions
dim = 5
gapfreq = 0.25
w = makeMap(dim, dim, gapfreq)   # a square graph
print(w.nodes())
# the list of the assigned packages, change the second value for num of pkgs
pkgList = addPackages(w, 3)
location = rand.choice(w.nodes())
#print("Vehicle Location {0} and Package location is at {1} " .format(location, pkgList.getNodeStartLocation()))
vehicle = truck.Vehicle(location, [], location)
for pkgLocation in pkgList:
    print("PkgStart: {0}, PkgEnd: {1}" .format(pkgLocation.getNodeStartLocation(), pkgLocation.getNodeEndLocation()))

print("Vehicle Start location: {0}" .format(vehicle.getCurrLocation()))
mySearch = Search.Search()
mySearch.search(prob.Problem(w), State.State(vehicle, pkgList, []))
draw(w)
