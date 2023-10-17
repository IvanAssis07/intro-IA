import numpy as np

GOAL_STATE = np.array([1,2,3,4,5,6,7,8,0])

def misplacedTiles(state):
  misCount = 0

  for i in range(len(state)):
    if state[i] != GOAL_STATE[i]:
      misCount += 1

  return misCount