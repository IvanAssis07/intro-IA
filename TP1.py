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

def executeAlgorithm(algorithm, showSteps, isTest):
	if (algorithm == "B"):
		bfs(eightPuzzle, showSteps, isTest)
	elif (algorithm == "I"):
		ids(eightPuzzle, showSteps, isTest)
	elif (algorithm == "U"):
		ucs(eightPuzzle, showSteps, isTest)
	elif (algorithm == "A"):
		aStar(eightPuzzle, "manhattanDist", showSteps, isTest)
		# aStar(eightPuzzle, "misplacedTiles", showSteps, isTest)
	elif (algorithm == "G"):
		greedy(eightPuzzle, "manhattanDist", showSteps, isTest)
		# greedy(eightPuzzle, "misplacedTiles", showSteps, isTest)
		
def main():
	isTest = False
	algorithm, showSteps = getEntry()
	
	executeAlgorithm(algorithm, showSteps, isTest)

if __name__ == "__main__":
    main()