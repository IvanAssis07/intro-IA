import time
import numpy as np

from structures.queue import Queue
from structures.node import Node

GOAL_STATE = np.array([1,2,3,4,5,6,7,8,0])

def printExplored(explored):
  for i in range(len(explored)):
    print(explored[i].board[0:3])
    print(explored[i].board[3:6])
    print(explored[i].board[6:9])
    print('\n')

def bfs(initialState, printSteps, isTest):
  if isTest:
    startingTime = time.time()
    exploredNodes = 0

  frontier = Queue()
  explored = set()
  
  root = Node(initialState)
  frontier.enqueue(root)
  
  while not frontier.is_empty():
    currentNode = frontier.dequeue()
    explored.add(currentNode)
    if isTest:
      exploredNodes += 1

    if currentNode.goalTest():
      if printSteps:
        currentNode.printPath()
      if isTest:
        executionTime = time.time() - startingTime
        print("Exec time:", executionTime, "Explored nodes:", exploredNodes)
      return
    
    currentNode.expandNode(heuristic = None)

    for i in range(len(currentNode.children)):
      if currentNode.children[i].goalTest():
        if printSteps:
          currentNode.children[i].printPath()
        if isTest:
          executionTime = time.time() - startingTime
          print("Exec time:", executionTime, "Explored nodes:", exploredNodes)
        return

      if currentNode.children[i] not in explored:
        frontier.enqueue(currentNode.children[i])
  
  return 