import sys

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

    if strategy == 'bfs':
        from BFS import bfs
        solution, stats = bfs(initial_layout, parameter)
    # elif strategy == 'dfs':
    #     from DFS import dfs
    #     solution, stats = dfs(initial_layout, parameter)
    # elif strategy == 'astr':
    #     from AStar import astar
    #     solution, stats = astar(initial_layout, parameter)
    else:
        print(f"Nieznana strategia: {strategy}")
        sys.exit(1)


if __name__ == "__main__":
    main()