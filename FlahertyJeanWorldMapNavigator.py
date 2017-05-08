###########################################################################
#                            World Map Navigator                          #
#                                                                         #
#  Programmed by Jean Flaherty (12-03-2016)                               #
#  Instructor:  Dean Zeller                                               #
#                                                                         #
#   Search algorithms adapted from:                                       #
#       MIT OCW 6.01SC Lecture 12 by Leslie Kaelbling                     # 
#       MIT OCW 6.01SC Lecture 13 by Leslie Kaelbling                     # 
#       MIT OCW 6.034 Lecture 4 by Patrick H. Winston                     #                                                                       #
#                                                                         #
#                                                                         #
#  Description:  The file contains code for search algorithms, animating  #
#                the search process, and mapping out nodes on the world   #
#                map.                                                     #
#                                                                         #
#  Objects:                                                               #
#                                                                         #
#       SearchNode      An object that represents a node with info about  #
#                       how the node was found by a search algorithm.     #
#                                                                         #
#       Stack           A collection data type that adds items to the end #
#                       of the collection and removes them from the       #
#                       end as well. Last in first out.                   #
#                                                                         #
#       Queue           A collection data type that adds items to the end #
#                       of the collection and removes them from the       #
#                       front. First in first out.                        #
#                                                                         #
#       SearchAlgorithm This class defines the different types of search  #
#                       algorithms that are implemented as an             #
#                       enumeration. It can even be converted to a        #
#                       string with str().                                #
#                                                                         #
#       SearchResult    A named tuple that is used for the return value   #
#                       of the search algorithms.                         #
#                                                                         #
#       Navigator       Handles defining the web of nodes, drawing a map  #
#                       of the nodes, using search algoritms, and         #
#                       animating the process of finding a path with      #
#                       search algorithms.                                #
#                                                                         #
#  This program is copyright (c) 2016 Jean Flaherty and Dean Zeller.      #
#  All rights reserved.  Permission granted to use and modify for         #
#  educational purposes only.  Any commercial use of this code must       #
#  receive permission from the author(s).                                 #
###########################################################################
from tkinter import *
import math
import datetime
from collections import namedtuple
from enum import Enum
from FlahertyJeanWorldMap import world_map
from FlahertyJeanAnimation import Animation

###########################################################################
# SearchNode: an object that represents a node with info about how the    #
#             node was found.                                             #
#                                                                         #
#   Adapted from: MIT OCW 6.01SC Lecture 12 by Leslie Kaelbling           #                                                                       #
#                                                                         #
#                                                                         #
#   Parameters:                                                           #
#           action  how the node relates to its parent.                   #
#                   which action was taken from the parent node.          #
#           state   the identity or name of the node.                     #
#           parent  the parent of the search node.                        #
#                                                                         #
###########################################################################
class SearchNode:
    #######################################################################
    #  Initialize search node.                                            #
    #######################################################################
    def __init__ (self, action, state, parent, actionCost=0):
        self.action = action
        self.state = state
        self.parent = parent
        if self.parent:
            self.cost = self.parent.cost + actionCost
        else:
            self.cost = actionCost

    #######################################################################
    #  Path: Returns path of the search node.                             #
    #######################################################################
    def path(self):
        if self.parent == None: return [(self.action, self.state)]
        else: return self.parent.path() + [(self.action, self.state)]

    #######################################################################
    #  InPath: checks if state is in path. So we can avoid going to the   #
    #       same node twice.                                              #
    #######################################################################
    def inPath(self, state):
        if self.state == state:
            return True
        elif self.parent == None:
            return False
        else:
            return self.parent.inPath(state)

###########################################################################
# Stack: a collection data type that adds items to the end of the         #
#    collection and removes them from the end as well. Last in first out. #
#                                                                         #
#   Adapted from: MIT OCW 6.01SC Lecture 12 by Leslie Kaelbling           #                                                                       #
#                                                                         #                         #
###########################################################################
class Stack:
    def __init__(self):
        self.data = []
    def push(self, item):
        self.data.append(item)
    def pop(self):
        return self.data.pop()
    def empty(self):
        return self.data is []

###########################################################################
# Queue: a collection data type that adds items to the end of the         #
#        collection and removes them from the front. First in first out.  # 
#                                                                         #
#   Adapted from: MIT OCW 6.01SC Lecture 12 by Leslie Kaelbling           #                                                                       #
#                                                                         #               #                              #
###########################################################################
class Queue:
    def __init__(self):
        self.data = []
    def push(self, item):
        self.data.append(item)
    def pop(self):
        return self.data.pop(0)
    def empty(self):
        return self.data is []

###########################################################################
# Priority Queue: a collection data type that adds items to the end of the#
#        collection and removes the lowest cost items first.              # 
#                                                                         #
#   Adapted from: MIT OCW 6.01SC Lecture 13 by Leslie Kaelbling           #                                                                       #
#                                                                         #                             #
###########################################################################
class PriorityQueue:
    def __init__(self):
        self.data = []
    def push(self, item, cost):
        self.data.append((cost, item))
    def pop(self):
        index = self.cheapItemIndex()
        return self.data.pop(index)[1] # just return the data item
    def empty(self):
        return len(self.data) == 0
    def cheapItemIndex(self):
        result = 0; lowestCost = self.data[0][0]
        for i in range(len(self.data)):
            (cost, item) = self.data[i]
            if cost < lowestCost:
                result, lowestCost = i, cost
        return result

###########################################################################
# SearchAlgorithm : This class defines the different types of search      #
#                   algorithms that are implemented as an enumeration. It #
#                   can even be converted to a string with str().         #
###########################################################################
class SearchAlgorithm(Enum):
    DEPTH_FIRST = 0
    DEPTH_FIRST_DYNAMIC = 1
    BREADTH_FIRST = 2
    BREADTH_FIRST_DYNAMIC = 3
    HILL_CLIMBING = 4
    UNIFORM_COST = 5
    UNIFORM_COST_DYNAMIC = 6
    A_STAR = 7

    # this allows the class to support str() converting
    def __str__(self):
        if self == SearchAlgorithm.DEPTH_FIRST:
            return "Depth First"
        elif self == SearchAlgorithm.DEPTH_FIRST_DYNAMIC:
            return "Depth First Dynamic"
        elif self == SearchAlgorithm.BREADTH_FIRST:
            return "Breadth First"
        elif self == SearchAlgorithm.BREADTH_FIRST_DYNAMIC:
            return "Breadth First Dynamic"
        elif self == SearchAlgorithm.HILL_CLIMBING:
            return "Hill Climbing"
        elif self == SearchAlgorithm.UNIFORM_COST:
            return "Uniform Cost"
        elif self == SearchAlgorithm.UNIFORM_COST_DYNAMIC:
            return "Uniform Cost Dynamic"
        elif self == SearchAlgorithm.A_STAR:
            return "A*"

###########################################################################
# SearchResult: A named tuple that is used for the return value of the    #
#               search algorithms.                                        #
#                                                                         #
#   path -- the path that the search function found.                      #
#   log -- a list of nodes that were considered before finding the path.  #                                                 #
#                                                                         #
###########################################################################
SearchResult = namedtuple('SearchResult', 'path log')

###########################################################################
# SearchDepthFirst : The depth first algorithm picks one direction and    #
#                    sticks to it until it meets a dead end. Slowly it    #
#                   works backwards until it figures out what went wrong. #
#                                                                         #
#   Adapted from: MIT OCW 6.01SC Lecture 12 by Leslie Kaelbling           #                                                                       #
#                                                                         #
#   parameters:                                                           #
#       initialState -- the starting point of the search                  #
#       goalTest -- a function that takes a state and returns 1 if it is  #
#                   the state that is desired, otherwise returns 0        #
#       successors -- a dictionary with all states as a keys and and a    #
#           list of connecting states as the value                        #
#       successor -- a function that takes a state and an action (0,1,2..)#
#           and returns another state, the successor                      #
#   return value: a SearchResult named tupel with path and log values     #
###########################################################################
def searchDepthFirst(initialState, goalTest, successors, successor):
    initialNode = SearchNode(None, initialState, None)
    # if we are already there look no further
    if goalTest(initialState): 
        return SearchResult(initialNode.path, [initialNode])
    agenda = Stack()
    agenda.push(initialNode)
    log = []
    # keep looking until there is nothing to search
    while not agenda.empty():
        parent = agenda.pop()
        newChildStates = []
        successors_count = len(successors[parent.state])
        for a in range(successors_count):
            newState = successor(parent.state, a)
            newNode = SearchNode(a, newState, parent)
            if goalTest(newState):
                # found it!
                log.append(newNode)
                return SearchResult(newNode.path(), log)
            elif newState in newChildStates: # pruning rule 2
                pass
            elif parent.inPath(newState):    # pruning rule 1
                pass
            else:
                log.append(newNode)
                newChildStates.append(newState)
                agenda.push(newNode)
    return SearchResult(None, log)

###########################################################################
# SearchDepthFirstAvoidVisited : The depth first algorithm picks one      #
#        direction and sticks to it until it meets a dead end. Slowly it  #
#        works backwards until it figures out what went wrong.            #
#                                                                         #
#   Adapted from: MIT OCW 6.01SC Lecture 12 by Leslie Kaelbling           #                                                                       #
#                                                                         #
#   parameters:                                                           #
#       initialState -- the starting point of the search                  #
#       goalTest -- a function that takes a state and returns 1 if it is  #
#                   the state that is desired, otherwise returns 0        #
#       successors -- a dictionary with all states as a keys and and a    #
#           list of connecting states as the value                        #
#       successor -- a function that takes a state and an action (0,1,2..)#
#           and returns another state, the successor                      #
#   return value: a SearchResult named tupel with path and log values     #
###########################################################################
def searchDepthFirstAvoidVisited(initialState, goalTest, successors, successor):
    initialNode = SearchNode(None, initialState, None)
    # if we are already there look no further
    if goalTest(initialState): 
        return SearchResult(initialNode.path, [initialNode])
    agenda = Stack()
    agenda.push(initialNode)
    visited = {initialState: True}
    log = []
    while not agenda.empty():
        parent = agenda.pop()
        successors_count = len(successors[parent.state])
        for a in range(successors_count):
            newState = successor(parent.state, a)
            newNode = SearchNode(a, newState, parent)
            if goalTest(newState):
                # found it!
                log.append(newNode)
                return SearchResult(newNode.path(), log)
            elif newState in visited: # pruning rule 1,2,3
                pass
            else:
                log.append(newNode)
                visited[newState] = True
                agenda.push(newNode)
    return SearchResult(None, log)

###########################################################################
# SearchBreadthFirst : The breadth first algorithm checks level by level  #
#       starting by searching all nodes one node away then two nodes away #
#       and keeps going untill the goal is reached.                       #
#                                                                         #
#   Adapted from: MIT OCW 6.01SC Lecture 12 by Leslie Kaelbling           #                                                                       #
#                                                                         #
#   parameters:                                                           #
#       initialState -- the starting point of the search                  #
#       goalTest -- a function that takes a state and returns 1 if it is  #
#                   the state that is desired, otherwise returns 0        #
#       successors -- a dictionary with all states as a keys and and a    #
#           list of connecting states as the value                        #
#       successor -- a function that takes a state and an action (0,1,2..)#
#           and returns another state, the successor                      #
#   return value: a SearchResult named tupel with path and log values     #
###########################################################################
def searchBreadthFirst(initialState, goalTest, successors, successor):
    initialNode = SearchNode(None, initialState, None)
    # if we are already there look no further
    if goalTest(initialState): 
        return SearchResult(initialNode.path, [initialNode])
    agenda = Queue()
    agenda.push(initialNode)
    log = []
    while not agenda.empty():
        parent = agenda.pop()
        newChildStates = []
        successors_count = len(successors[parent.state])
        for a in range(successors_count):
            newState = successor(parent.state, a)
            newNode = SearchNode(a, newState, parent)
            if goalTest(newState):
                # found it!
                log.append(newNode)
                return SearchResult(newNode.path(), log)
            elif newState in newChildStates: # pruning rule 2
                pass
            elif parent.inPath(newState):    # pruning rule 1
                pass
            else:
                log.append(newNode)
                newChildStates.append(newState)
                agenda.push(newNode)
    return SearchResult(None, log)

###########################################################################
# SearchBreadthFirstDynamicProgramming : The dynamic breadth first        #
#           algorithm does what the breadth first algorithm does without  #
#           repeating nodes that have already been checked. This speeds   #
#           things up immensely.                                          #
#                                                                         #
#   Adapted from: MIT OCW 6.01SC Lecture 12 by Leslie Kaelbling           #                                                                       #
#                                                                         #
#   parameters:                                                           #
#       initialState -- the starting point of the search                  #
#       goalTest -- a function that takes a state and returns 1 if it is  #
#                   the state that is desired, otherwise returns 0        #
#       successors -- a dictionary with all states as a keys and and a    #
#           list of connecting states as the value                        #
#       successor -- a function that takes a state and an action (0,1,2..)#
#           and returns another state, the successor                      #
#   return value: a SearchResult named tupel with path and log values     #
###########################################################################
def searchBreadthFirstDynamicProgramming(initialState, goalTest, successors, successor):
    agenda = Queue()
    if goalTest(initialState):
        return [(None, initialState)]
    agenda.push(SearchNode(None, initialState, None))
    visited = {initialState: True}
    log = []
    while not agenda.empty():
        parent = agenda.pop()
        successors_count = len(successors[parent.state])
        for a in range(successors_count):
            newState = successor(parent.state, a)
            newNode = SearchNode(a, newState, parent)
            if goalTest(newState):
                # found it!
                log.append(newNode)
                return SearchResult(newNode.path(), log)
            elif newState in visited: # rules 1, 2, 3
                pass
            else:
                log.append(newNode)
                visited[newState] = True
                agenda.push(newNode)
    return SearchResult(None, log)

###########################################################################
# SearchHillClimbing : The hill climbing algorithm compares each adjacent #
#       node to see which one is closer to our goal effectively avoiding  #
#       searching in the wrong direction. Unfortunately sometimes it      #
#       reaches a local minima and assumes it can't go further.           # 
#                                                                         #
#   Adapted from: MIT OCW 6.034 Lecture 4 -- Patrick H. Winston           # 
#                                                                         #                                            #
#   parameters:                                                           #
#       initialState -- the starting point of the search                  #
#       goalTest -- a function that takes a state and returns 1 if it is  #
#                   the state that is desired, otherwise returns 0        #
#       successors -- a dictionary with all states as a keys and and a    #
#           list of connecting states as the value                        #
#       successor -- a function that takes a state and an action (0,1,2..)#
#           and returns another state, the successor                      #
#       better -- a function that takes two nodes and returnes the node   #
#           that is "better" or is closer to your goal.                   #
#   return value: a SearchResult named tupel with path and log values     #
###########################################################################
def searchHillClimbing(initialState, goalTest, successors, successor, better):
    agenda = Stack()
    if goalTest(initialState):
        return [(None, initialState)]
    agenda.push(SearchNode(None, initialState, None))
    log = []
    while not agenda.empty():
        parent = agenda.pop()
        newChildStates = []
        successors_count = len(successors[parent.state])
        closestNode = parent
        for a in range(successors_count):
            newState = successor(parent.state, a)
            newNode = SearchNode(a, newState, parent)
            if goalTest(newState):
                # found it!
                log.append(newNode)
                return SearchResult(newNode.path(), log)
            elif newState in newChildStates: # pruning rule 2
                pass
            elif parent.inPath(newState):    # pruning rule 1
                pass
            else:
                log.append(newNode)
                closestNode = better(newNode, closestNode)
        if closestNode == parent:
            log.append(parent)
            return SearchResult(parent.path(), log)
        
        agenda.push(closestNode)
    return SearchResult(None, log)


###########################################################################
# SearchUniformCost: The uniform cost algorithm prioritizes low cost paths#
#                                                                         #
#   Adapted from: MIT OCW 6.01SC Lecture 13 by Leslie Kaelbling           #                                                                       #
#                                                                         #
#   parameters:                                                           #
#       initialState -- the starting point of the search                  #
#       goalTest -- a function that takes a state and returns 1 if it is  #
#                   the state that is desired, otherwise returns 0        #
#       successors -- a dictionary with all states as a keys and and a    #
#           list of connecting states as the value                        #
#       successorAndCost -- a function that takes a state and an action   #
#           and returnscthe successor and the cost of the action          #
#   return value: a SearchResult named tupel with path and log values     #
###########################################################################
def searchUniformCost(initialState, goalTest, successors, successorAndCost):
    startNode = SearchNode(None, initialState, None, 0)
    agenda = PriorityQueue()
    if goalTest(initialState):
        return [(None, initialState)]
    agenda.push(startNode, 0)
    log = []
    while not agenda.empty():
        parent = agenda.pop()
        successors_count = len(successors[parent.state])
        if goalTest(parent.state):
            log.append(parent)
            return SearchResult(parent.path(), log)
        for a in range(successors_count):
            (newState, cost) = successorAndCost(parent.state, a)
            if not parent.inPath(newState):
                newNode = SearchNode(a, newState, parent, cost)
                log.append(newNode)
                agenda.push(newNode, newNode.cost)
                
    return SearchResult(None, log)

###########################################################################
# SearchUniformCostDynamic: The uniform cost algorithm prioritizes low    #
#       cost paths. It will keep track of states that it already expanded.#                                                                      #
#                                                                         #
#   Adapted from: MIT OCW 6.01SC Lecture 13 by Leslie Kaelbling           #                                                                       #
#                                                                         #
#   parameters:                                                           #
#       initialState -- the starting point of the search                  #
#       goalTest -- a function that takes a state and returns 1 if it is  #
#                   the state that is desired, otherwise returns 0        #
#       successors -- a dictionary with all states as a keys and and a    #
#           list of connecting states as the value                        #
#       successorAndCost -- a function that takes a state and an action   #
#           and returnscthe successor and the cost of the action          #
#   return value: a SearchResult named tupel with path and log values     #
###########################################################################
def searchUniformCostDynamic(initialState, goalTest, successors, successorAndCost):
    startNode = SearchNode(None, initialState, None, 0)
    agenda = PriorityQueue()
    if goalTest(initialState):
        return [(None, initialState)]
    agenda.push(startNode, 0)
    expanded = {}
    log = []
    while not agenda.empty():
        parent = agenda.pop()
        if not parent.state in expanded:
            expanded[parent.state] = True
            successors_count = len(successors[parent.state])
            if goalTest(parent.state):
                log.append(parent)
                return SearchResult(parent.path(), log)
            for a in range(successors_count):
                (newState, cost) = successorAndCost(parent.state, a)
                if not newState in expanded:
                    newNode = SearchNode(a, newState, parent, cost)
                    log.append(newNode)
                    agenda.push(newNode, newNode.cost)
                
    return SearchResult(None, log)


###########################################################################
# SearchAStar: The uniform cost algorithm prioritizes low    #
#       cost paths. It will keep track of states that it already expanded.#                                                                      #
#                                                                         #
#   Adapted from: MIT OCW 6.01SC Lecture 13 by Leslie Kaelbling           #                                                                       #
#                                                                         #
#   parameters:                                                           #
#       initialState -- the starting point of the search                  #
#       goalTest -- a function that takes a state and returns 1 if it is  #
#                   the state that is desired, otherwise returns 0        #
#       successors -- a dictionary with all states as a keys and and a    #
#           list of connecting states as the value                        #
#       successorAndCost -- a function that takes a state and an action   #
#           and returnscthe successor and the cost of the action          #
#       heuristic -- a function that estimates the cheapest remaining     #
#           cost of the path between a node and the final node            #
#   return value: a SearchResult named tupel with path and log values     #
###########################################################################
def searchAStar(initialState, goalTest, successors, successorAndCost, heuristic):
    startNode = SearchNode(None, initialState, None, 0)
    if goalTest(initialState):
        return [(None, initialState)]
    agenda = PriorityQueue()
    agenda.push(startNode, 0)
    expanded = {}
    log = []
    while not agenda.empty():
        parent = agenda.pop()
        if not parent.state in expanded:
            expanded[parent.state] = True
            successors_count = len(successors[parent.state])
            if goalTest(parent.state):
                log.append(parent)
                return SearchResult(parent.path(), log)
            for a in range(successors_count):
                (newState, cost) = successorAndCost(parent.state, a)
                if not newState in expanded:
                    newNode = SearchNode(a, newState, parent, cost)
                    log.append(newNode)
                    #print("S:{} H:{} C:{}".format(newState, heuristic(newState), newNode.cost))
                    agenda.push(newNode, newNode.cost + heuristic(newState))
                
    return SearchResult(None, log)

###########################################################################
# Navigator : this class handles defining the web of nodes, drawing a map #
#       of the nodes, using search algoritms, and animating the process   #
#       of finding a path with search algorithms.                         #                                     #
###########################################################################
class Navigator:
    # define default values
    initialState = "Colorado"
    finalState = "Japan"
    searchAlgorithm = SearchAlgorithm.DEPTH_FIRST
    # define the connections between nodes
    successors = {
            "Anchorage"     : ["Vancouver", "Quebec"],
            "Bangkok"       : ["China", "Darwin"],
            "Cape Horn"     : ["Machu Picchu", "Rio"],
            "China"         : ["Bangkok", "East Russia", "Mongolia", "Mumbai"],
            "Colombia"      : ["Machu Picchu", "Mexico", "Rio"],
            "Colorado"      : ["New York", "San Francisco"],
            "Darwin"        : ["Bangkok","Perth", "Sydney"],
            "East Russia"   : ["China", "Mongolia","Moscow"],
            "Egypt"         : ["Morrocco", "South Africa", "Nigeria", "Israel"],
            "Greenland"     : ["Paris", "Quebec"],
            "Israel"        : ["Italy", "Egypt", "Mongolia", "Mumbai"],
            "Italy"         : ["Paris", "Spain", "Moscow", "Israel"],
            "Japan"         : ["Sydney"],
            "Machu Picchu"  : ["Cape Horn", "Colombia"],
            "Mexico"        : ["San Francisco", "Colombia"],
            "Mongolia"      : ["Moscow", "Israel", "China", "East Russia"],
            "Morrocco"      : ["Spain", "Nigeria", "Egypt"],
            "Moscow"        : ["Paris", "Italy", "Mongolia", "East Russia"],
            "Mumbai"        : ["Israel", "China"],
            "New York"      : ["Colorado", "Quebec"],
            "Nigeria"       : ["Rio", "South Africa", "Morrocco", "Egypt"],
            "Paris"         : ["Spain", "Greenland", "Italy", "Moscow"],
            "Perth"         : ["Darwin", "Sydney"],
            "Quebec"        : ["Anchorage", "New York", "Greenland", "Vancouver"],
            "Rio"           : ["Cape Horn", "Nigeria", "Colombia"],
            "San Francisco" : ["Vancouver", "Colorado", "Mexico"],
            "South Africa"  : ["Nigeria", "Egypt"],
            "Spain"         : ["Italy", "Paris", "Morrocco"],
            "Sydney"        : ["Perth", "Darwin", "Japan"],
            "Vancouver"     : ["Anchorage", "San Francisco", "Quebec"]
        }
    # define the coordinates of the nodes
    coordinates = {
            "Anchorage"     : (15,107),
            "Bangkok"       : (335,203),
            "Cape Horn"     : (100,320),
            "China"         : (315,153),
            "Colombia"      : (85,210),
            "Colorado"      : (56,149),
            "Darwin"        : (375,255),
            "East Russia"   : (370,100),
            "Egypt"         : (232,190),
            "Greenland"     : (141,105),
            "Israel"        : (245,167),
            "Italy"         : (215,141),
            "Japan"         : (367,155),
            "Machu Picchu"  : (93,260),
            "Mexico"        : (58,194),
            "Mongolia"      : (310,123),
            "Morrocco"      : (180,167),
            "Moscow"        : (255,103),
            "Mumbai"        : (291,180),
            "New York"      : (90,145),
            "Nigeria"       : (205,210),
            "Paris"         : (195,130),
            "Perth"         : (348,285),
            "Quebec"        : (105,115),
            "Rio"           : (133,240),
            "San Francisco" : (32,160),
            "South Africa"  : (213,290),
            "Spain"         : (186,147),
            "Sydney"        : (395,280),
            "Vancouver"     : (33,130),
        }
    
    #######################################################################
    #  Search: applies the correct search algorithm specified by the      #
    #        searchAlgorithm attribute. Uses initialState and finalState  #
    #        attributes of the Navigator object to use for parameters of  #
    #        the search algorithms. Returns search result                 #                                      #
    #######################################################################
    def search(self):
        # create the functions to use as parameters of the search algorithm

        ###################################################################
        # goalTest: return true if state is the final state               #
        ###################################################################
        def goalTest(state):
            return state==self.finalState

        ###################################################################
        # distance: calculates the distance between node and goal         #
        ###################################################################
        def distance(state1, state2):
            x1 = self.coordinates[state1][0]
            y1 = self.coordinates[state1][1]
            x2 = self.coordinates[state2][0]
            y2 = self.coordinates[state2][1]
            # calculate distance for x and y axis
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            # use the pythagorean theorem
            return math.sqrt(dx*dx+dy*dy)
        
        ###################################################################
        # better: takes two nodes and returns the node closer to goal     #
        ###################################################################
        def better(node1, node2):
            # compare the two distanced and return closer node
            if distance(node1.state, self.finalState) < distance(node2.state,self.finalState):
                return node1
            else:
                return node2

        ###################################################################
        # successor: return state or "neighbor" in specified "direction"  #
        #       or action.                                                #
        ###################################################################
        def successor(state, action):
            if action < len(self.successors[state]):
                return self.successors[state][action]
            else:
                return state

        
        def successorAndCost(state, action):
            if action < len(self.successors[state]):
                successor = self.successors[state][action]
                cost = distance(successor, state)
                return (successor, cost)
            else:
                return (state, 0)

        def heuristic(state):
            return distance(state, self.finalState)

        # use the correct algorithm and return search result
        if self.searchAlgorithm == SearchAlgorithm.DEPTH_FIRST:
            return searchDepthFirst(self.initialState, goalTest, self.successors, successor)
        elif self.searchAlgorithm == SearchAlgorithm.DEPTH_FIRST_DYNAMIC:
            return searchDepthFirstAvoidVisited(self.initialState, goalTest, self.successors, successor)
        elif self.searchAlgorithm == SearchAlgorithm.BREADTH_FIRST:
            return searchBreadthFirst(self.initialState, goalTest, self.successors, successor)
        elif self.searchAlgorithm == SearchAlgorithm.BREADTH_FIRST_DYNAMIC:
            return searchBreadthFirstDynamicProgramming(self.initialState, goalTest, self.successors, successor)
        elif self.searchAlgorithm == SearchAlgorithm.HILL_CLIMBING:
            return searchHillClimbing(self.initialState, goalTest, self.successors, successor, better)
        elif self.searchAlgorithm == SearchAlgorithm.UNIFORM_COST:
            return searchUniformCost(self.initialState, goalTest, self.successors, successorAndCost)
        elif self.searchAlgorithm == SearchAlgorithm.UNIFORM_COST_DYNAMIC:
            return searchUniformCostDynamic(self.initialState, goalTest, self.successors, successorAndCost)
        elif self.searchAlgorithm == SearchAlgorithm.A_STAR:
            return searchAStar(self.initialState, goalTest, self.successors, successorAndCost, heuristic)
    
    #######################################################################
    #  AnimateSearchLog: animates the process that the search algorithm   #
    #       takes to find the path.                                       #
    #######################################################################
    def animateSearchLog(self, c, log, completion, fpms=50):
        animation = Animation(c)
        def logAnimation(i):
            self.drawSearchNode(c, log[i])
        animation.timeline = logAnimation
        animation.frame_count = len(log)
        animation.fpms = fpms
        animation.completion = completion
        animation.play()

    #######################################################################
    #  CordinatesFromPath: returns a list of coordinates that define the  #
    #       path.                                                         #
    #######################################################################
    def coordinatesFromPath(self, path):
        resultCoordinates = []
        for (action, state) in path:
            x = self.coordinates[state][0]
            y = self.coordinates[state][1]
            coordinate = (x,y)
            resultCoordinates.append(coordinate)
        return resultCoordinates

    #######################################################################
    #  DrawSearchNode: draws the path of the search node.                 #                                                      #
    #######################################################################
    def drawSearchNode(self, c, node):
        coordinates = self.coordinatesFromPath(node.path())
        c.delete("node")
        c.create_line(coordinates, fill="red", tag="node")

    #######################################################################
    #  DrawNetwork: draws all nodes and the connections between them.     #                                                      #
    #######################################################################
    def drawNetwork(self, c, tag="network"):
        for key, value in self.coordinates.items():
            # get the coordinate values
            x = value[0]
            y = value[1]
            # draw a dot for the node
            c.create_oval(x-1, y-1, x+1, y+1, fill="#500", outline="#500")
            # loop through all successors or "neighbors"
            for successor in self.successors[key]:
                # get the cordinate values of the "neighbors"
                x2 = self.coordinates[successor][0]
                y2 = self.coordinates[successor][1]
                # draw the line connecting the node with its "neighbors"
                c.create_line(x, y, x2, y2, fill="#500")

