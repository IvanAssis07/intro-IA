from structures.stack import Stack
from structures.node import Node
import numpy as np

GOAL_STATE = np.array([1,2,3,4,5,6,7,8,0])

def misplacedTiles(state):
  misCount = 0

  for i in range(len(state)):
    if state[i] != GOAL_STATE[i]:
      misCount += 1

  return misCount

def findIdx(state, value):
  idx = np.where(state == value)[0][0]
  row = idx // 3
  column = idx - row * 3

  return row, column

def manhattanDistance(state):
  heuristic = 0

  for i in range(len(state)):
    row, column = findIdx(state, i)
    goalRow, goalColumn = findIdx(GOAL_STATE, i)

    heuristic += abs(row - goalRow) + abs(column - goalColumn)

  return heuristic

def aStar(initialState, heuristic):
  print("A*")
  frontier = Stack()
  explored = set()
  path = []

  root = Node(initialState)
  frontier.push(root)

  while frontier.is_empty() == False:
    currentNode = frontier.pop()
    explored.add(currentNode)

    if currentNode.goalTest():
      path.append(currentNode)
      return path

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