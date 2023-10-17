import numpy as np

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
    
    def moveRight(self, state, zeroIdx):
      if (zeroIdx % 3 < 2):
        copyPuzzle = np.copy(state)

        copyPuzzle[zeroIdx], copyPuzzle[zeroIdx + 1] = copyPuzzle[zeroIdx + 1], copyPuzzle[zeroIdx]
        
        child = Node(copyPuzzle)
        self.children.append(child)
        child.parent = self
        child.depth = self.depth + 1 

    def moveLeft(self, state, zeroIdx):
      if (zeroIdx % 3 > 0):
        copyPuzzle = np.copy(state)

        copyPuzzle[zeroIdx], copyPuzzle[zeroIdx - 1] = copyPuzzle[zeroIdx - 1], copyPuzzle[zeroIdx]
      
        child = Node(copyPuzzle)
        self.children.append(child)
        child.parent = self  
        child.depth = self.depth + 1

    def moveDown(self, state, zeroIdx):
      if (zeroIdx < 6):
        copyPuzzle = np.copy(state)

        copyPuzzle[zeroIdx], copyPuzzle[zeroIdx + 3] = copyPuzzle[zeroIdx + 3], copyPuzzle[zeroIdx]
      
        child = Node(copyPuzzle)
        self.children.append(child)
        child.parent = self
        child.depth = self.depth + 1          

    def moveUp(self, state, index):
      if (index > 2):
        copyPuzzle = np.copy(state)

        copyPuzzle[index], copyPuzzle[index - 3] = copyPuzzle[index - 3], copyPuzzle[index]
      
        child = Node(copyPuzzle)
        self.children.append(child)
        child.parent = self
        child.depth = self.depth + 1
    
    def expandNode(self):
      self.moveDown(self.board, self.zeroIdx)
      self.moveUp(self.board, self.zeroIdx)
      self.moveRight(self.board, self.zeroIdx)
      self.moveLeft(self.board, self.zeroIdx)
    
    def goalTest(self):
      for i in range(len(self.board)):
         if self.board[i] != goalState[i]:
           return False
      return True
    
