from typing import List, Tuple


#zastanowić się czy int jest okej
class PuzzleState:
    def __init__(self, board: List[List[int]], zero_pos: Tuple[int, int] = None, path: str = ""):
        self.board = board
        self.path = path
        self.zero_pos = zero_pos if zero_pos is not None else self.find_zero_pos()
        self.cost = len(path)
        self.f = 0

        # Jeśli zero_pos nie jest podane, obliczamy je
        if zero_pos is None:
            self.zero_pos = self.find_zero_pos()
        else:
            self.zero_pos = zero_pos

    def find_zero_pos(self) -> Tuple[int, int]:
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return i, j
        return None

    def is_goal(self) -> bool:
        w, k = len(self.board), len(self.board[0])

        goal = [[(i * k + j + 1) % (w * k) for j in range(k)] for i in range(w)] #można zapisać czytelniej...

        return self.board == goal


    def __hash__(self):
        return hash(tuple(num for row in self.board for num in row))

    def __eq__(self, other):
        return self.board == other.board

    def __lt__(self, other):
        return self.f < other.f

    def get_neighbours(self, parameter: str = "UDLR") -> List['PuzzleState']:
        neighbours = []
        directions_map = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }

        x, y = self.zero_pos

        for move in parameter:
            dx, dy = directions_map[move]
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < len(self.board) and 0 <= new_y < len(self.board[0]):
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbours.append(PuzzleState(new_board, (new_x, new_y), self.path + move))

        return neighbours

    def heuristic(self, method: str) -> int:
        if method == "hamm":
            return self.hamming()
        elif method == "manh":
            return self.manhattan()
        else:
            raise ValueError(f"Unknown heuristic method: {method}")

    def manhattan(self) -> int:
        distance = 0
        w, k = len(self.board), len(self.board[0])
        for i in range(w):
            for j in range(k):
                value = self.board[i][j]
                if value != 0:
                    target_x = (value - 1) // k
                    target_y = (value - 1) % k
                    distance += abs(target_x - i) + abs(target_y - j)
        return distance

    def hamming(self) -> int:
        count = 0
        w, k = len(self.board), len(self.board[0])
        for i in range(w):
            for j in range(k):
                expected = ( i * k + j + 1) % (w * k)
                if self.board[i][j] != 0 and self.board[i][j] != expected:
                    count += 1
        return count
