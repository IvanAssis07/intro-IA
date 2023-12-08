import time
import numpy as np

from structures.stack import Stack
from structures.node import Node

def greedy(initialState, heuristic, printSteps, isTest):
  if isTest:
    startingTime = time.time()
    exploredNodes = 0

  root = Node(initialState)
  frontier = []
  frontier.append(root)

  explored = set()

  while (len(frontier) > 0):
    frontier.sort(key = lambda x: x.heuristic)
    currentNode = frontier.pop(0)

    if isTest:
      exploredNodes += 1
      
    if currentNode.goalTest():
      if printSteps:
        currentNode.printPath()
      if isTest:
        executionTime = time.time() - startingTime
        print("Exec time:", executionTime, "Explored nodes:", exploredNodes, "H:", heuristic)
      return
    
    explored.add(currentNode)
    currentNode.expandNode(heuristic)

    for i in range(len(currentNode.children)):
      if currentNode.children[i] not in explored or currentNode.children[i] not in frontier:
        frontier.append(currentNode.children[i])
      elif currentNode.children[i] in frontier and currentNode.children[i].heuristic < frontier[frontier.index(currentNode.children[i])].heuristic:
        frontier.remove(currentNode.children[i])
        frontier.append(currentNode.children[i])

  print("No solution found")
  return