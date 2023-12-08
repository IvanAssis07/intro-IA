import time
import numpy as np

from structures.queue import Queue
from structures.node import Node

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

    if currentNode.goalTest():
      if printSteps:
        currentNode.printPath()
      if isTest:
        executionTime = time.time() - startingTime
        print(" Exec time:", executionTime, "Explored nodes:", exploredNodes)
      return
    
    currentNode.expandNode(heuristic = None)
    
    if isTest:
      exploredNodes += 1

    for i in range(len(currentNode.children)):
      if currentNode.children[i].goalTest():
        if printSteps:
          currentNode.children[i].printPath()
        if isTest:
          executionTime = time.time() - startingTime
          print("Exec time:", executionTime, ",Explored nodes:", exploredNodes)
        return

      if currentNode.children[i] not in explored:
        frontier.enqueue(currentNode.children[i])
  
  print("No solution found")
  return 