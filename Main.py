import sys
from PuzzleState import PuzzleState

def load_initial_layout(filename):
    # Wczytanie układu początkowego z pliku
    with open(filename, 'r') as file:
        w, k = map(int, file.readline().strip().split())
        layout = []
        for _ in range(w):
            row = list(map(int, file.readline().strip().split()))
            if len(row) != k:
                raise ValueError("Nieprawidłowa liczba elementów w wierszu.")
            layout.append(row)
    return layout, w, k

def save_solution(solution, filename):
    with open(filename, 'w') as file:
        if solution == "Fail":
            file.write("-1/n")
        else:
            file.write(f"{len(solution)}\n")  # Długość rozwiązania
            file.write(solution + "\n")  # Ciąg ruchów

def save_stats(filename,solution, visited_count, processed_count, max_depth, time_taken):
    with open(filename, 'w') as file:
        file.write(f"{len(solution) if solution != 'Fail' else -1}\n")  # Długość rozwiązania
        file.write(f"{visited_count}\n")  # Liczba odwiedzonych stanów
        file.write(f"{processed_count}\n")  # Liczba przetworzonych stanów
        file.write(f"{max_depth}\n")  # Maksymalna głębokość
        file.write(f"{time_taken:.3f}\n")  # Czas trwania w sekundach, zaokrąglony do 3 miejsc


def main():
    # Sprawdzenie liczby argumentów
    if len(sys.argv) != 6:
        print("Użycie: python solver.py <strategy> <param> <input_file> <solution_file> <stats_file>")
        sys.exit(1)

    # Rozpakowanie argumentów
    strategy = sys.argv[1]
    parameter = sys.argv[2]
    input_file = sys.argv[3]
    solution_file = sys.argv[4]
    stats_file = sys.argv[5]

    # Wczytanie planszy
    initial_layout, w, k = load_initial_layout(input_file)
    initial_state = PuzzleState(initial_layout)

    if strategy == 'bfs':
        from BFS import bfs
        solution, visited_count, processed_count, max_depth, time_taken = bfs(initial_state, parameter)
        save_solution(solution, solution_file)
        save_stats(stats_file, solution, visited_count, processed_count, max_depth, time_taken)
    elif strategy == 'dfs':
        from DFS import dfs
        solution, visited_count, processed_count, max_depth, time_taken = dfs(initial_state, parameter)
        save_solution(solution, solution_file)
        save_stats(stats_file, solution, visited_count, processed_count, max_depth, time_taken)
    # elif strategy == 'astr':
    #     from AStar import astar
    #     solution, stats = astar(initial_layout, parameter)
    else:
        print(f"Nieznana strategia: {strategy}")
        sys.exit(1)


if __name__ == "__main__":
    main()