import time
from typing import Union, Tuple

from PuzzleState import PuzzleState

MAX_DEPTH = 20  # maksymalna dozwolona głębokość

def dfs(start: PuzzleState, parameter: str) -> Union[Tuple[str, int, int, int, float], str]:
    start_time = time.perf_counter()  # rozpoczęcie pomiaru czasu

    if start.is_goal():
        return start.path, 1, 1, 0, time.perf_counter() - start_time  # jeśli początek jest rozwiązaniem

    stack = [start] #open
    visited = set() #closed

    visited_count = 1
    processed_count = 0
    max_depth = 0

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)
            visited_count += 1
            processed_count += 1
            max_depth = max(max_depth, len(current.path))

            if len(current.path) >= MAX_DEPTH:
                continue  # pomijamy dalsze rozwijanie tego węzła

            neighbors = current.get_neighbours(parameter)
            neighbors.reverse()

            for neighbor in neighbors:
                if neighbor.is_goal():
                    return neighbor.path, visited_count, processed_count, max_depth, time.perf_counter() - start_time
                stack.append(neighbor)
                visited_count += 1

    return "Fail", visited_count, processed_count, max_depth, time.perf_counter() - start_time  # brak rozwiązania
