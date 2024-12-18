import numpy as np

from structures.heuristcs import manhattanDistance, misplacedTiles
from structures.stack import Stack

goalState = np.array([1,2,3,4,5,6,7,8,0])
class Node:
    def __init__(self, data):
        self.board = data
        self.strBoard = str(data)
        self.depth = 0
        self.parent = None
        self.children = []
        self.zeroIdx = np.where(data == 0)[0][0]
        self.cost = 0
        self.heuristic = 0

    def __str__(self):
      result = ""
      for i in range(0, 9):
        if i % 3 == 0 and i != 0:
            result += "\n"
        if (self.zeroIdx == i):
          result += "  "
        else:
          result += f"{self.board[i]} "
      result += "\n"
      return result
    
    def __hash__(self):
      return hash(self.strBoard)
    
    def __eq__(self, other):
        return isinstance(other, Node) and self.strBoard == other.strBoard
    
    def printPath(self):
      steps = 0
      path = Stack()
      path.push(self)
      node = self.parent
      
      while node is not None:
        steps += 1
        path.push(node)
        node = node.parent

      print(steps, "\n")
      while not path.is_empty():
        node = path.pop()
        print(node)
    
    def moveRight(self, heuristic):
      if (self.zeroIdx % 3 < 2):
        copyPuzzle = np.copy(self.board)

        copyPuzzle[self.zeroIdx], copyPuzzle[self.zeroIdx + 1] = copyPuzzle[self.zeroIdx + 1], copyPuzzle[self.zeroIdx]
        
        child = Node(copyPuzzle)
        self.children.append(child)
        child.parent = self
        child.depth = self.depth + 1 

        if (heuristic != None and heuristic == "manhattanDistance"):
          hsValue = manhattanDistance(copyPuzzle)
          child.cost = hsValue + child.depth #A* 
          child.heuristic = hsValue #Greedy
        elif (heuristic != None and heuristic == "misplacedTiles"):
          hsValue = misplacedTiles(copyPuzzle)
          child.cost = hsValue + child.depth #A* 
          child.heuristic = hsValue #Greedy

    def moveLeft(self, heuristic):
      if (self.zeroIdx % 3 > 0):
        copyPuzzle = np.copy(self.board)

        copyPuzzle[self.zeroIdx], copyPuzzle[self.zeroIdx - 1] = copyPuzzle[self.zeroIdx - 1], copyPuzzle[self.zeroIdx]
      
        child = Node(copyPuzzle)
        self.children.append(child)
        child.parent = self  
        child.depth = self.depth + 1

        if (heuristic != None and heuristic == "manhattanDistance"):
          hsValue = manhattanDistance(copyPuzzle)
          child.cost = hsValue + child.depth #A* 
          child.heuristic = hsValue #Greedy
        elif (heuristic != None and heuristic == "misplacedTiles"):
          hsValue = misplacedTiles(copyPuzzle)
          child.cost = hsValue + child.depth #A* 
          child.heuristic = hsValue #Greedy

    def moveDown(self, heuristic):
      if (self.zeroIdx < 6):
        copyPuzzle = np.copy(self.board)

        copyPuzzle[self.zeroIdx], copyPuzzle[self.zeroIdx + 3] = copyPuzzle[self.zeroIdx + 3], copyPuzzle[self.zeroIdx]
      
        child = Node(copyPuzzle)
        self.children.append(child)
        child.parent = self
        child.depth = self.depth + 1 

        if (heuristic != None and heuristic == "manhattanDistance"):
          hsValue = manhattanDistance(copyPuzzle)
          child.cost = hsValue + child.depth #A* 
          child.heuristic = hsValue #Greedy
        elif (heuristic != None and heuristic == "misplacedTiles"):
          hsValue = misplacedTiles(copyPuzzle)
          child.cost = hsValue + child.depth #A* 
          child.heuristic = hsValue #Greedy         

    def moveUp(self, heuristic):
      if (self.zeroIdx > 2):
        copyPuzzle = np.copy(self.board)

        copyPuzzle[self.zeroIdx], copyPuzzle[self.zeroIdx - 3] = copyPuzzle[self.zeroIdx - 3], copyPuzzle[self.zeroIdx]
      
        child = Node(copyPuzzle)
        self.children.append(child)
        child.parent = self
        child.depth = self.depth + 1

        if (heuristic != None and heuristic == "manhattanDistance"):
          hsValue = manhattanDistance(copyPuzzle)
          child.cost = hsValue + child.depth #A* 
          child.heuristic = hsValue #Greedy
        elif (heuristic != None and heuristic == "misplacedTiles"):
          hsValue = misplacedTiles(copyPuzzle)
          child.cost = hsValue + child.depth #A* 
          child.heuristic = hsValue #Greedy
    
    def expandNode(self, heuristic):
      self.moveDown(heuristic)
      self.moveUp(heuristic)
      self.moveRight(heuristic)
      self.moveLeft(heuristic)
    
    def goalTest(self):
      for i in range(len(self.board)):
         if self.board[i] != goalState[i]:
           return False
      return True
    
