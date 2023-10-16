import sys
import numpy as np

from searchAlgorithms.bfs import bfs
from searchAlgorithms.ids import ids

eightPuzzle = np.zeros(9, dtype=int)
showIterations = False

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
          
	if (type(sys.argv[-1]) is not int):
		showIterations = True

	print(f"Algorithm: {algorithm}")
	print(f"Print Steps: {showIterations}")

def printPath(path):
  while len(path) > 0:
    board = path.pop().board
    print(board[0:3])
    print(board[3:6])
    print(board[6:9], "\n")

def main():
	getEntry()

	path = bfs(eightPuzzle)
	path = ids(eightPuzzle)

	if (len(path) == 0):
		print("No solution found")
	else:
		print(f"Solution found with {len(path) - 1} steps")
		printPath(path)

if __name__ == "__main__":
    main()