import time
import numpy as np

from structures.stack import Stack
from structures.node import Node

def ucs(initialState, printSteps, isTest):
  if isTest:
    startingTime = time.time()
    exploredNodes = 0
    
  root = Node(initialState)
  frontier = []
  frontier.append(root)
  explored = set()

  while (len(frontier) > 0):
    frontier.sort(key = lambda x: x.depth)
    currentNode = frontier.pop(0)
    
    if isTest:
      exploredNodes += 1

    if currentNode.goalTest():
      if printSteps:
        currentNode.printPath()
      if isTest:
        executionTime = time.time() - startingTime
        print("Exec time:", executionTime, "Explored nodes:", exploredNodes)
      return  
    
    explored.add(currentNode)
    currentNode.expandNode(None)

    for i in range(len(currentNode.children)):
      if currentNode.children[i] not in explored or currentNode.children[i] not in frontier:
        frontier.append(currentNode.children[i])
      elif currentNode.children[i] in frontier and currentNode.children[i].depth < frontier[frontier.index(currentNode.children[i])].depth:
        frontier.remove(currentNode.children[i])
        frontier.append(currentNode.children[i])
  
  print("No solution found")
  return
  
