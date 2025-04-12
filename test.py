from PuzzleState import PuzzleState
from BFS import bfs

initial_board = [
    [1, 2, 3, 4],
    [5, 7, 8, 0],
    [9, 6, 11, 12],
    [13, 10, 14, 15]
]
parameter = "RLUD"

start_state = PuzzleState(initial_board)
solution = bfs(start_state, parameter)

print("Found solution:", solution)