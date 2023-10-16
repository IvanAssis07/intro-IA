from structures.queue import Queue
from structures.node import Node
import numpy as np

GOAL_STATE = np.array([1,2,3,4,5,6,7,8,0])

def printExplored(explored):
  for i in range(len(explored)):
    print(explored[i].board[0:3])
    print(explored[i].board[3:6])
    print(explored[i].board[6:9])
    print('\n')

def bfs(initialState):
  frontier = Queue()
  explored = set()
  path = []
  
  root = Node(initialState)
  frontier.enqueue(root)

  while not frontier.is_empty():
    currentNode = frontier.dequeue()
    explored.add(currentNode)
    # print(currentNode, currentNode.zeroIdx)
    
    if currentNode.goalTest():
      path.append(currentNode)
      return path
    
    currentNode.expandNode()

    for i in range(len(currentNode.children)):
      if currentNode.children[i].goalTest():
        print(currentNode)
        path.append(currentNode.children[i])
        path.append(currentNode)

        while currentNode.parent != None:
          path.append(currentNode.parent)
          currentNode = currentNode.parent
        return path[::-1]

      if currentNode.children[i] not in explored:
        frontier.enqueue(currentNode.children[i])
  
  return path