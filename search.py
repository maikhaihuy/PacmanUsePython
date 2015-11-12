# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from util import Stack

    # Get start state
    startState = problem.getStartState()
    startNode = (startState, "", 0)
    # Visited position
    visted = []
    # Stack contain on state of Pacman
    stackNode = Stack()
    stackNode.push((startNode, []))

    while(not stackNode.isEmpty()):
        # Get current node executing
        currentNode = stackNode.pop()
        print "Current node ", currentNode
        valueNode = currentNode[0]
        path = currentNode[1]

        # Check node isnt visited
        if valueNode[0] not in visted:
            # Add node into list of visited
            visted.append(valueNode[0])
            # Check current node is Goal?
            if problem.isGoalState(valueNode[0]) == True:
                return path
            # Not goal
            else:
                seccessors = problem.getSuccessors(valueNode[0])
                for seccessor in seccessors:
                    if seccessor[0] not in visted:
                        tempPath = list(path)
                        tempPath.append(seccessor[1])
                        stackNode.push((seccessor,tempPath))
    return  path

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    startState = problem.getStartState()
    startNode = (startState, "", 0)
    # Visited
    visited = set([startState])
    # Declare variable for queue node
    queueNode = Queue()
    # Push start state into queue
    queueNode.push((startNode,[]))

    while(not queueNode.isEmpty()):
        currentNode = queueNode.pop()
        #print "Current node ", currentNode
        valueNode = currentNode[0]

        path = currentNode[1]

        if problem.isGoalState(valueNode[0]):
            print "Results ", path
            return path
        else:
            seccessors = problem.getSuccessors(valueNode[0])
            #print "\tSeccessors ", seccessors
            
            for seccessor in seccessors:
                if seccessor[0] not in visited:
                    tempPath = list(path)
                    visited.add(seccessor[0])
                    tempPath.append(seccessor[1])
                    queueNode.push((seccessor,tempPath))
                    #print "\tTemp path ", tempPath


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    startState = problem.getStartState()
    startNode = (startState, "", 0)
    # Visited
    visited = set([startState])
    # Declare priority queue
    priorityQueueNode = PriorityQueue()
    # Start state
    priorityQueueNode.push((startNode,[]),0)

    # Cost
    cost = 0
    while not priorityQueueNode.isEmpty():
        currentNode = priorityQueueNode.pop()
        #print currentNode
        valueNode = currentNode[0]
        path = currentNode[1]
        cost = valueNode[2]
        #print "Current node ", currentNode
        if problem.isGoalState(valueNode[0]):
            return path
        else:
            seccessors = problem.getSuccessors(valueNode[0])
            #print "\tSeccessors ", seccessors

            for seccessor in seccessors:
                if seccessor[0] not in visited:
                    tempPath = list(path)
                    visited.add(seccessor[0])
                    tempPath.append(seccessor[1])
                    priorityQueueNode.push((seccessor, tempPath), cost + seccessor[2])


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
