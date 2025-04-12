import time
from collections import deque
from typing import Any

from PuzzleState import PuzzleState


def dfs(start: PuzzleState, parameter: str) -> tuple[str, int, int, int, float] | str | Any:
    start_time = time.perf_counter()  # rozpoczęcie pomiaru czasu

    if start.is_goal():
        return start.path, 1, 1, 0, time.perf_counter() - start_time  # jeśli początek jest rozwiązaniem

    stack = [start]
    visited = set()

    visited_count = 0
    processed_count = 0
    max_depth = 0

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            visited_count += 1
            processed_count += 1
            max_depth = max(max_depth, len(current.path))

            neighbors = current.get_neighbours(parameter)
            neighbors.reverse()  # ważne dla DFS, by zachować kolejność zgodną ze schematem

            for neighbor in neighbors:
                if neighbor.is_goal():
                    return neighbor.path, visited_count, processed_count, max_depth, time.perf_counter() - start_time
                stack.append(neighbor)

    return "Fail", visited_count, processed_count, max_depth, time.perf_counter() - start_time  # brak rozwiązania
