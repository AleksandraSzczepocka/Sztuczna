from typing import List, Tuple
from collections import deque

#zastanowić się czy int jest okej
class PuzzleState:
    def __init__(self, board: List[List[int]], zero_pos: Tuple[int, int] = None, path: str = "",
                 parameter: str = "LRUD"):
        # Inicjalizacja planszy i ścieżki
        self.board = board
        self.path = path  # np. "LDUR"
        self.parameter = parameter

        # Jeśli zero_pos nie jest podane, obliczamy je
        if zero_pos is None:
            self.zero_pos = self.find_zero_pos()
        else:
            self.zero_pos = zero_pos

    def find_zero_pos(self) -> Tuple[int, int]:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

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
        directions_map = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }

        x, y = self.zero_pos

        for move in self.parameter:
            dx, dy = directions_map[move]
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < len(self.board) and 0 <= new_y < len(self.board[0]):
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbours.append(PuzzleState(new_board, (new_x, new_y), self.path + move, self.parameter))

        return neighbours


