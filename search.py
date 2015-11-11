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
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    results = []
    from util import Stack

    # Get start state
    stateStart = problem.getStartState()
    # Visited position
    visted = []
    # Stack contain on state of Pacman
    stackNode = Stack()
    stackNode.push((stateStart, "", 0))
    # Stack tracking
    stackTracking = Stack()

    # Step
    step = 1
    while(not stackNode.isEmpty()):
        # Get current node executing
        currentNode = stackNode.pop()

        # Check node isnt visited
        if currentNode[0] not in visted:
            # Add node into list of visited
            visted.append(currentNode[0])
            # Check current node is Goal?
            if problem.isGoalState(currentNode[0]) == True:
                stackTracking.push(currentNode)
                while(not stackTracking.isEmpty()):
                    action = stackTracking.pop()[1]
                    if action != "":
                        results.insert(0,action)
                print results
                return results
            # Not goal
            else:
                # Variable for deadlock position 
                isStuck = True
                # While is stucking, pop nodes, is pushed
                while True:
                    print "Step ", step
                    step += 1
                    print "\tCurrent node", currentNode
                    seccessors = problem.getSuccessors(currentNode[0])
                    for seccessor in seccessors:
                        if seccessor[0] not in visted:
                            isStuck = False
                            print "\tSeccessors ", seccessor
                            stackNode.push(seccessor)

                    if isStuck == True:
                        temp = stackTracking.pop()
                        print "Remove step ", step
                        step -= 1
                        print "\tNode ", temp
                        currentNode = temp
                    else:
                        stackTracking.push(currentNode)
                        break
                    
    return  results

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    startState = problem.getStartState()
    startNode = (startState, "", "")
    # Visited
    visited = set([startState])
    # Declare variable for queue node
    queueNode = Queue()
    # Push start state into queue
    queueNode.push((startState,[]))

    while(not queueNode.isEmpty()):
        currentNode = queueNode.pop()
        valueNode = currentNode[0]
        path = currentNode[1]

        if problem.isGoalState(valueNode[1]):
            return path
        else:
            seccessors = problem.getSuccessors(currentNode[0])
            tempPath = list(path)
            for seccessor in seccessors:
                if seccessor[0] not in visited:
                    visited.add(seccessor[0])
                    queue.push(seccessor)
                    tempPath.append(seccessor[1])
                    queueNode.push(seccessor,tempPath)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

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
