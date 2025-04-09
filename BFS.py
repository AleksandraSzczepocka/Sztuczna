from collections import deque

import PuzzleState

def bfs(start: PuzzleState)-> str:
    if start.is_goal():
        return start.path

    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)

    while queue:
        current = queue.popleft()

        for neighbor in current.get_neighbours():
            if neighbor not in visited:
                if neighbor.is_goal():
                    return neighbor.path
                queue.append(neighbor)
                visited.add(neighbor)

    return "Fail" # można poprawić to