import numpy as np

GOAL_STATE = np.array([1,2,3,4,5,6,7,8,0])

def findIdx(state, value):
  idx = np.where(state == value)[0][0]
  row = idx // 3
  column = idx - row * 3

  return row, column

def manhattanDistance(state):
  heuristic = 0

  for i in range(len(state)):
    row, column = findIdx(state, i)
    goalRow, goalColumn = findIdx(GOAL_STATE, i)

    heuristic += abs(row - goalRow) + abs(column - goalColumn)

  return heuristic