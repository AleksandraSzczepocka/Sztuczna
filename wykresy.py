import os
import pandas as pd
import matplotlib.pyplot as plt

# Ścieżka do katalogu z plikami (zmień jeśli trzeba)
folder = "./stats"

# Lista wyników
results = []

# Przechodzimy po plikach
for filename in os.listdir(folder):
    if filename.endswith("_stats.txt"):
        parts = filename.split("_")
        if len(parts) < 6:
            continue  # niepoprawny format

        depth = int(parts[1])
        method = parts[3].upper()
        variant = parts[4].upper()

        # Wczytaj dane z pliku
        with open(os.path.join(folder, filename), "r") as f:
            lines = f.read().strip().split("\n")
            if len(lines) != 5:
                continue  # niepoprawna zawartość

            # Parsuj dane
            length = int(lines[0])
            visited = int(lines[1])
            processed = int(lines[2])
            max_depth = int(lines[3])
            time = float(lines[4])

            # Dodaj do listy
            results.append({
                "depth": depth,
                "method": method,
                "variant": variant,
                "length": length,
                "visited": visited,
                "processed": processed,
                "max_depth": max_depth,
                "time": time
            })

# Zamień na DataFrame
df = pd.DataFrame(results)

# Czyszczenie kolumn z ewentualnych spacji
df.columns = [str(col).strip() for col in df.columns]

if df.empty:
    print("❌ Brak danych! Sprawdź folder i zawartość plików.")
    exit()

print("✅ Wczytano dane. Kolumny:", df.columns)


# Mapa nazw kryteriów
criteria = {
    'length': 'Długość rozwiązania',
    'visited': 'Liczba stanów odwiedzonych',
    'processed': 'Liczba stanów przetworzonych',
    'max_depth': 'Maks. głębokość rekursji',
    'time': 'Czas trwania (s)'
}

# Rysowanie wykresów
for criterion, crit in criteria.items():
    filtered_df = df.copy()
    if criterion == 'length':
        filtered_df = filtered_df[filtered_df['length'] != -1]

    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # Ogółem BFS, DFS, A*
    ax = axs[0, 0]
    avg_general = df.groupby(['depth', 'method'])[criterion].mean().unstack()
    avg_general.rename(columns={'ASTR': 'A*'}, inplace=True)
    avg_general.plot(kind='bar', ax=ax)
    ax.tick_params(axis='x', labelrotation=0, labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    ax.legend(title=None)
    ax.set_title("Ogółem", fontsize=16)
    ax.set_ylabel(crit, fontsize=14)
    ax.set_xlabel("")
    if criterion not in ['max_depth', 'length']:
        ax.set_yscale('log')

    # A* - heurystyki
    ax = axs[0, 1]
    astar_df = df[df['method'] == 'ASTR']
    if not astar_df.empty:
        # Podmień skróty na pełne nazwy
        heuristic_names = {
            "HAMM": "Hamming",
            "MANH": "Manhattan"
        }
        astar_df = astar_df.copy()
        astar_df['variant'] = astar_df['variant'].map(heuristic_names).fillna(astar_df['variant'])

        avg_astar = astar_df.groupby(['depth', 'variant'])[criterion].mean().unstack()
        avg_astar.plot(kind='bar', ax=ax)
        ax.tick_params(axis='x', labelrotation=0, labelsize=12)
        ax.tick_params(axis='y', labelsize=12)
        ax.legend(title=None)
        if criterion == 'time':
            ax.set_ylim(bottom=0.0009)
    ax.set_title("A*", fontsize=16)
    ax.set_xlabel("")

    # BFS - porządki
    ax = axs[1, 0]
    bfs_df = df[df['method'] == 'BFS']
    if not bfs_df.empty:
        avg_bfs = bfs_df.groupby(['depth', 'variant'])[criterion].mean().unstack()
        avg_bfs.plot(kind='bar', ax=ax)
        ax.tick_params(axis='x', labelrotation=0, labelsize=12)
        ax.tick_params(axis='y', labelsize=12)
        ax.legend(title=None)
    ax.set_title("BFS", fontsize=16)
    ax.set_ylabel(crit, fontsize=14)
    ax.set_xlabel("Głębokość", fontsize=14)
    if criterion not in ['max_depth', 'length']:
        ax.set_yscale('log')

    # DFS - porządki
    ax = axs[1, 1]
    dfs_df = df[df['method'] == 'DFS']
    if not dfs_df.empty:
        avg_dfs = dfs_df.groupby(['depth', 'variant'])[criterion].mean().unstack()
        avg_dfs.plot(kind='bar', ax=ax)
        ax.tick_params(axis='x', labelrotation=0, labelsize=12)
        ax.tick_params(axis='y', labelsize=12)
        ax.legend(title=None)
    ax.set_title("DFS", fontsize=16)
    ax.set_xlabel("Głębokość", fontsize=14)
    if criterion not in ['max_depth', 'length']:
        ax.set_yscale('log')

    plt.tight_layout()
    plt.subplots_adjust(top=0.88)
    plt.show()
