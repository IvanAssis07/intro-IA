from structures.stack import Stack
from structures.node import Node
import numpy as np

GOAL_STATE = np.array([1,2,3,4,5,6,7,8,0])

def dls(initialState, limit):
  frontier = Stack()
  explored = set()
  result = None

  root = Node(initialState)
  frontier.push(root)

  while frontier.is_empty() == False:
    currentNode = frontier.pop()
    explored.add(currentNode)

    if currentNode.goalTest():
      result = currentNode

    if currentNode.depth < limit:
      currentNode.expandNode()

      for i in range(len(currentNode.children)):
        if currentNode.children[i] not in explored:
          frontier.push(currentNode.children[i])
  
  return result

def ids(initialState):
  print("IDS")
  limit = 0
  result = None
  path = []

  while result == None:
    result = dls(initialState, limit)
    limit += 1

  if result.depth != 0:
    while result.parent != None:
      path.append(result)
      result = result.parent
    path.append(result)
  else:
    path.append(result)

  return path[::-1]