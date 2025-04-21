import math
import time
import heapq
from typing import Tuple, Union
from Utils import round_up_3


from PuzzleState import PuzzleState


def astar(start: PuzzleState, parameter: str) -> Union[Tuple[str, int, int, int, float], str]:
    start_time = time.perf_counter()

    if start.is_goal():
        return start.path, 1, 0, 0, round_up_3(time.perf_counter() - start_time)

    priority_queue = []
    heapq.heappush(priority_queue, (start.cost + start.heuristic(parameter), start))

    closed_set = set()
    visited_count = 0
    processed_count = 0
    max_depth = 0

    while priority_queue:
        _, current = heapq.heappop(priority_queue)

        if current not in closed_set:
            if current.is_goal():
                max_depth = max(max_depth, len(current.path))
                return current.path, visited_count, processed_count, max_depth, round_up_3(time.perf_counter() - start_time)

            closed_set.add(current)
            visited_count += 1
            max_depth = max(max_depth, len(current.path))

            neighbors = current.get_neighbours()

            for neighbor in neighbors:
                if neighbor not in closed_set:
                    neighbor.f = neighbor.cost + neighbor.heuristic(parameter)
                    heapq.heappush(priority_queue, (neighbor.f, neighbor))

            processed_count += 1

    return "Fail", visited_count, processed_count, max_depth, round_up_3(time.perf_counter() - start_time)
