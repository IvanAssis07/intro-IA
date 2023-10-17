from structures.stack import Stack
from structures.node import Node
import numpy as np

GOAL_STATE = np.array([1,2,3,4,5,6,7,8,0])

def ucs(initialState):
  print("UCS")
  root = Node(initialState)
  frontier = []
  frontier.append(root)
  explored = set()
  path = []

  while (len(frontier) > 0):
    frontier.sort(key = lambda x: x.depth)
    currentNode = frontier.pop(0)
    
    if currentNode.goalTest():
      path.append(currentNode)

      while currentNode.parent != None:
        path.append(currentNode.parent)
        currentNode = currentNode.parent
      return path
    
    explored.add(currentNode)

    currentNode.expandNode()

    for i in range(len(currentNode.children)):
      if currentNode.children[i] not in explored or currentNode.children[i] not in frontier:
        frontier.append(currentNode.children[i])
      elif currentNode.children[i] in frontier and currentNode.children[i].depth < frontier[frontier.index(currentNode.children[i])].depth:
        frontier.remove(currentNode.children[i])
        frontier.append(currentNode.children[i])
  
  return path
  