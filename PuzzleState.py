from typing import List, Tuple
from collections import deque

#zastanowić się czy int jest okej
class PuzzleState:
    def __init__(self, board: List[List[int]], zero_pos: Tuple[int, int], path: str = ""):
        self.board = board
        self.zero_pos = zero_pos  # row i col, gdzie znajduje się zero
        self.path = path  # np. "LDUR"

    def is_goal(self) -> bool:
        goal = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]
        return self.board == goal


    def __hash__(self):
        return hash(tuple(num for row in self.board for num in row))

    def __eq__(self, other):
        return self.board == other.board

