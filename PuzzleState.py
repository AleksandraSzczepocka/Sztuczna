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

    def get_neighbours(self) -> List['PuzzleState']:
        neighbours = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        x, y = self.zero_pos

        for direction in directions:
            mx, my = directions[direction]
            new_x, new_y = x + mx, y + my

            if 0 <= new_x < len(self.board) and 0 <= new_y < len(self.board[0]):
                new_board = [row[:] for row in self.board]

                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]

                neighbours.append(PuzzleState(new_board, (new_x, new_y), self.path + direction))

            return neighbours


