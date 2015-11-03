# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

def bfs(graph, start, goal):
    raise NotImplementedError

## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    raise NotImplementedError


## Now we're going to add some heuristics into the search.  
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    #graph.get_heuristic(start, goal) .get_connected_nodes(node) .get_edge(node1,node2) .are_connected(node1, node2) graph.is_valid_path(path):
    currentNode = start
    path = [start]
    agenda = []
    while(currentNode is not None):
        connectedNodes = graph.get_connected_nodes(currentNode)
        distanceDict = []
        for pathExtension in sorted((node for node in connectedNodes if (node not in agenda and node not in path)), key=lambda x: (graph.get_heuristic(x, goal)), reverse=True):
            #Add each of these guys to the agenda in order
            pathCopy = path[:]
            if(pathExtension == goal):
                path.append(pathExtension)
                return path
            pathCopy.append(pathExtension)
            agenda.append([pathExtension, pathCopy])
        if(len(agenda) > 0):
            nextOnAgenda = agenda.pop()
            currentNode = nextOnAgenda[0][:]
            path = nextOnAgenda[1][:]
        else:
            currentNode = None
    return path

#Expected: ['F', 'B', 'D', 'C', 'E', 'G']

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the 
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    raise NotImplementedError

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.

def path_length(graph, node_names):
    pathLen = 0
    numNodes = len(node_names)
    if(numNodes > 1):
        for index in range(numNodes-1):
            #Get this node in the list and then figure out how to get to the next node in the list
            node1 = node_names[index]
            node2 = node_names[index+1]
            edgeFound = graph.get_edge(node1,node2)
            if(not edgeFound is None):
                pathLen += edgeFound.length
    return pathLen


def branch_and_bound(graph, start, goal):
    raise NotImplementedError

def a_star(graph, start, goal):
    #graph.get_heuristic(start, goal) .get_connected_nodes(node) .get_edge(node1,node2) .are_connected(node1, node2) graph.is_valid_path(path):
    #each time we run through a star, we're going to calculate the total distance
    currentNode = start
    path = [start]
    extendedSet = []
    agenda = []
    while(currentNode is not None):
        connectedNodes = graph.get_connected_nodes(currentNode)
        distanceDict = []
        for pathExtension in (node for node in connectedNodes if (node not in extendedSet)):
            #Add each of these guys to the agenda in order
            totalDistanceEstimate = graph.get_heuristic(pathExtension, goal) + path_length(graph,path+[pathExtension])
            if(pathExtension == goal):
                path.append(pathExtension)
                return path
            agenda.append([totalDistanceEstimate, path+[pathExtension]])
        if(len(agenda) > 0):
            agenda.sort(key=lambda x: (x[0], x[1]), reverse=True)
            nextOnAgenda = agenda.pop()
            currentNode = nextOnAgenda[1][-1]
            extendedSet.append(currentNode)
            path = nextOnAgenda[1][:]
        else:
            currentNode = None
    return path


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''
