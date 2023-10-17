import sys
import numpy as np

from searchAlgorithms.bfs import bfs
from searchAlgorithms.ids import ids
from searchAlgorithms.ucs import ucs
from searchAlgorithms.aStar import aStar
from searchAlgorithms.greedy import greedy

eightPuzzle = np.zeros(9, dtype=int)

def getEntry():
  if len(sys.argv) < 2:
    print("Usage: python TP1.py <algorithm> <input_configuration> [PRINT]")
    sys.exit(1)

  # Pegando o Algoritmo que será utilizado
  algorithm = sys.argv[1]

  # Pegando a configuração inicial
  count = 2

  for i in range(9):
    eightPuzzle[i] = int(sys.argv[count])
    count += 1

  if sys.argv[-1] == "PRINT":
    showSteps = True
  else:
    showSteps = False
    
  return algorithm, showSteps

def executeAlgorithm(algorithm, showSteps):
	# B, I, U, A, G, H
	if (algorithm == "B"):
		bfs(initialState=eightPuzzle, printSteps=showSteps)
	elif (algorithm == "I"):
		ids(initialState=eightPuzzle)
	elif (algorithm == "U"):
		ucs(initialState=eightPuzzle)
	elif (algorithm == "A"):
		aStar(initialState=eightPuzzle, heuristic="manhattanDist")
		# aStar(initialState=eightPuzzle, heuristic="misplacedTiles")
	elif (algorithm == "G"):
		greedy(initialState=eightPuzzle, heuristic="manhattanDist")
		# greedy(initialState=eightPuzzle, heuristic="misplacedTiles")
		
def main():
	algorithm, showSteps = getEntry()
	
	executeAlgorithm(algorithm, showSteps)

if __name__ == "__main__":
    main()