from PuzzleState import PuzzleState
from BFS import bfs

initial_board = [
    [1, 2, 3, 4],
    [5, 7, 8, 0],
    [9, 6, 11, 12],
    [13, 10, 14, 15]
]
parameter = "LRUD"

start_state = PuzzleState(initial_board, parameter=parameter)
solution = bfs(start_state)

print("Found solution:", solution)