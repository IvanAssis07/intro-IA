import numpy as np

from structures.stack import Stack
from structures.node import Node
from heuristics import manhattanDist, misplacedTiles

GOAL_STATE = np.array([1,2,3,4,5,6,7,8,0])

def defineHeuristic(heuristic, state):
  if heuristic == "manhattanDist":
    return manhattanDist(state)
  elif heuristic == "misplacedTiles":
    return misplacedTiles(state)

def aStar(initialState, heuristic):
  print("A*")
  root = Node(initialState)
  frontier = []
  frontier.append(root)

  explored = set()
  path = []

  while (len(frontier) > 0):
    frontier.sort(key = lambda x: x.cost)
    currentNode = frontier.pop(0)
    explored.add(currentNode)

    if currentNode.goalTest():
      path.append(currentNode)

      while currentNode.parent != None:
        path.append(currentNode.parent)
        currentNode = currentNode.parent
      return path

    explored.add(currentNode)
    
    currentNode.expandNode()

    for i in range(len(currentNode.children)):
      if currentNode.children[i].goalTest():
        path.append(currentNode.children[i])
        path.append(currentNode)

        while currentNode.parent != None:
          path.append(currentNode.parent)
          currentNode = currentNode.parent
        return path

      if currentNode.children[i] not in explored:
        frontier.push(currentNode.children[i])

  return path