import math
import time
from collections import deque
from typing import Union, Tuple
from Utils import round_up_3

from PuzzleState import PuzzleState


def bfs(start: PuzzleState, parameter: str) -> Union[Tuple[str, int, int, int, float], str]:
    start_time = time.perf_counter()  # początek pomiary czasu

    if start.is_goal():
        return start.path, 1, 0, 0, round_up_3(time.perf_counter() - start_time)


    closed_set = set() #closed
    open_queue = deque() #open
    open_queue.append(start)
    closed_set.add(start)

    processed_count = 0
    visited_count = 1
    max_depth = 0

    while open_queue:
        current = open_queue.popleft()

        processed_count += 1
        max_depth = max(max_depth, len(current.path))

        for neighbor in current.get_neighbours(parameter):
            if neighbor not in closed_set:
                if neighbor.is_goal():
                    max_depth = max(max_depth, len(neighbor.path))
                    return neighbor.path, visited_count, processed_count, round_up_3(time.perf_counter() - start_time)
                open_queue.append(neighbor)
                closed_set.add(neighbor)
                visited_count += 1

    return "Fail", visited_count, processed_count, max_depth, round_up_3(time.perf_counter() - start_time)  # Statystyki, gdy brak rozwiązania
