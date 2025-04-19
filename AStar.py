import time
import heapq
from typing import Any

from PuzzleState import PuzzleState


def astar(start: PuzzleState, parameter: str) -> tuple[str, int, int, int, float] | str | Any:
    start_time = time.perf_counter()

    if start.is_goal():
        return start.path, 1, 0, 0, time.perf_counter() - start_time

    priority_queue = []
    heapq.heappush(priority_queue, (start.cost + start.heuristic(parameter), start))

    visited = set()
    visited_count = 1
    processed_count = 0
    max_depth = 0

    while priority_queue:
        _, current = heapq.heappop(priority_queue)
        processed_count += 1
        max_depth = max(max_depth, len(current.path))

        if current not in visited:
            if current.is_goal():
                return current.path, visited_count, processed_count, max_depth, time.perf_counter() - start_time

            visited.add(current)
            visited_count += 1

            neighbors = current.get_neighbours()

            for neighbor in neighbors:
                if neighbor not in visited:
                    neighbor.f = neighbor.cost + neighbor.heuristic(parameter)
                    heapq.heappush(priority_queue, (neighbor.f, neighbor))
                    #visited_count += 1

    return "Fail", visited_count, processed_count, max_depth, time.perf_counter() - start_time
