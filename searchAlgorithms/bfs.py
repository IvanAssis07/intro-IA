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

def bfs(initialState, printSteps):
  frontier = Queue()
  explored = set()
  
  root = Node(initialState)
  frontier.enqueue(root)

  while not frontier.is_empty():
    currentNode = frontier.dequeue()
    explored.add(currentNode)
    
    if currentNode.goalTest():
      if printSteps:
        currentNode.printPath()
      return
    
    currentNode.expandNode(heuristic = None)

    for i in range(len(currentNode.children)):
      if currentNode.children[i].goalTest():
        if printSteps:
          currentNode.children[i].printPath()
        return

      if currentNode.children[i] not in explored:
        frontier.enqueue(currentNode.children[i])
  
  return 