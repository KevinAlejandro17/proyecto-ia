from collections import deque

# Definir la cuadrícula como un grafo
grid = [
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 5],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 4, 4, 4, 0, 1, 0],
    [2, 0, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 4, 4, 0, 0, 1, 1, 0],
    [0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 3, 0],
    [1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
]

# Definir movimientos posibles (arriba, abajo, izquierda, derecha)
movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(grid, start):
    queue = deque([start])
    visited = set()
    parent = {}

    while queue:
        current_node = queue.popleft()
        row, col = current_node

        if grid[row][col] == 3:  # Si encontramos a Grogu
            path = []
            while current_node != start:
                path.append(current_node)
                current_node = parent[current_node]
            path.append(start)
            return path[::-1]

        visited.add(current_node)

        for move in movimientos:
            new_row = row + move[0]
            new_col = col + move[1]
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and (new_row, new_col) not in visited and grid[new_row][new_col] != 1:
                queue.append((new_row, new_col))
                parent[(new_row, new_col)] = current_node

    return None  # Si no se encuentra un camino

# Encontrar el punto de inicio
start = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 2:
            start = (i, j)
            break
    if start:
        break

# Aplicar BFS
path = bfs(grid, start)

# Imprimir el camino
if path:
    print("El camino para encontrar a Grogu es:")
    for step in path:
        print(step)
else:
    print("No se encontró un camino para llegar a Grogu.")
