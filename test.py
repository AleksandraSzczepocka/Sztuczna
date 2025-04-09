from PuzzleState import PuzzleState
from BFS import bfs

initial_board = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 0, 12],
    [13, 14, 11, 15]
]
zero_position = (3, 2)
parameter = "LRUD"

start_state = PuzzleState(initial_board, zero_position, "", parameter)
solution = bfs(start_state)

print("Found solution:", solution)