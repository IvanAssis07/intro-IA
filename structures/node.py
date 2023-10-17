import numpy as np

from structures.heuristcs import manhattanDistance, misplacedTiles

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
        self.heuristic = None

    def __str__(self):
        return str(self.board)
    
    def __hash__(self):
      return hash(self.strBoard)
    
    def __eq__(self, other):
        return isinstance(other, Node) and self.strBoard == other.strBoard
    
    def moveRight(self, state, zeroIdx, heuristic):
      if (zeroIdx % 3 < 2):
        copyPuzzle = np.copy(state)

        copyPuzzle[zeroIdx], copyPuzzle[zeroIdx + 1] = copyPuzzle[zeroIdx + 1], copyPuzzle[zeroIdx]
        
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

    def moveLeft(self, state, zeroIdx, heuristic):
      if (zeroIdx % 3 > 0):
        copyPuzzle = np.copy(state)

        copyPuzzle[zeroIdx], copyPuzzle[zeroIdx - 1] = copyPuzzle[zeroIdx - 1], copyPuzzle[zeroIdx]
      
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

    def moveDown(self, state, zeroIdx, heuristic):
      if (zeroIdx < 6):
        copyPuzzle = np.copy(state)

        copyPuzzle[zeroIdx], copyPuzzle[zeroIdx + 3] = copyPuzzle[zeroIdx + 3], copyPuzzle[zeroIdx]
      
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

    def moveUp(self, state, index, heuristic):
      if (index > 2):
        copyPuzzle = np.copy(state)

        copyPuzzle[index], copyPuzzle[index - 3] = copyPuzzle[index - 3], copyPuzzle[index]
      
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
      self.moveDown(self.board, self.zeroIdx, heuristic)
      self.moveUp(self.board, self.zeroIdx, heuristic)
      self.moveRight(self.board, self.zeroIdx, heuristic)
      self.moveLeft(self.board, self.zeroIdx, heuristic)
    
    def goalTest(self):
      for i in range(len(self.board)):
         if self.board[i] != goalState[i]:
           return False
      return True
    
