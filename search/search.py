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

"""
Name: Ravi Grewal
Abstract: implementation of search algorithms for Pacman agents
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

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def generalSearch(problem, heuristic=nullHeuristic, search="dfs"):
    """
    General search algorithm
    :param problem: the search problem
    :param search: the search algorithm to use
    :param heuristic: heuristic to use
    :return: list of actions to reach goal state
    """
    if search == "dfs":
        fringe = util.Stack()
    elif search == "bfs":
        fringe = util.Queue()
    else:  # search is either a-star or ucs
        fringe = util.PriorityQueue()

    visited = set()
    startState = problem.getStartState()
    fringe.push((startState, [], 0)) if (search == "dfs" or search == "bfs") \
        else fringe.push((startState, [], 0), 0)

    # fringe entries are of the form: (start, [actions], cost)
    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()
        if problem.isGoalState(state):
            return actions
        if state not in visited:
            visited.add(state)
            for nextState, nextAction, nextCost in problem.getSuccessors(state):
                if nextState not in visited:
                    continuedPath = actions + [nextAction]
                    totalCost = cost + nextCost
                    if search == "dfs" or search == "bfs":
                        fringe.push((nextState, continuedPath, totalCost))
                    elif search == "ucs":
                        fringe.push((nextState, continuedPath, totalCost), totalCost)
                    elif search == "astar":
                        priority = totalCost + heuristic(nextState, problem)
                        fringe.push((nextState, continuedPath, totalCost), priority)


def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    return generalSearch(problem, search="dfs")

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    return generalSearch(problem, search="bfs")

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    return generalSearch(problem, search="ucs")

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    return generalSearch(problem, heuristic=heuristic, search="astar")


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
