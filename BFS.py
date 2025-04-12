import time
from collections import deque
from typing import Any

from PuzzleState import PuzzleState


def bfs(start: PuzzleState, parameter: str) -> tuple[str, int, int, int, float] | str | Any:
    start_time = time.perf_counter()  # początek pomiary czasu

    if start.is_goal():
        return start.path, 1, 1, 0, time.perf_counter() - start_time  # Statystyki przy natychmiastowym rozwiązaniu


    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)

    processed_count = 0
    visited_count = 1
    max_depth = 0

    while queue:
        current = queue.popleft()
        processed_count += 1
        max_depth = max(max_depth, len(current.path))

        for neighbor in current.get_neighbours(parameter):
            if neighbor not in visited:
                visited_count += 1
                if neighbor.is_goal():
                    return neighbor.path, visited_count, processed_count, max_depth, time.perf_counter() - start_time
                queue.append(neighbor)
                visited.add(neighbor)

    return "Fail", visited_count, processed_count, max_depth, time.perf_counter() - start_time  # Statystyki, gdy brak rozwiązania
