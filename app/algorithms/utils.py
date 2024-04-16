costo_basico_holder = [1]
costo_enemigo_holder = [5]
contador_movimientos = 0

def calcular_costo(grid, nuevo_estado):
    global contador_movimientos
    costo_basico = costo_basico_holder[0]
    costo_enemigo = costo_enemigo_holder[0]
    x, y = nuevo_estado
    if grid[x][y] == 0 or grid[x][y] == 5:
        return costo_basico
    elif grid[x][y] == 4:
        return costo_enemigo
    elif grid[x][y] == 3:
        costo_basico_holder[0] = 0.5
        costo_enemigo_holder[0] = 0.5
        contador_movimientos = 10
        return 1
    else:
        if contador_movimientos == 10:
            contador_movimientos -= 1
            return costo_basico
        else:
            costo_basico_holder[0] = 1
            costo_enemigo_holder[0] = 5
            return costo_basico


def reconstruir_ruta(nodo):
    ruta = []
    while nodo.padre:
        ruta.append(nodo.operador)
        nodo = nodo.padre
    return ruta[::-1]

def encontrar_estado_inicial(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                return (i, j)
    return None

def load_world(file_path):
    with open(file_path, 'r') as file:
        world = [list(map(int, line.strip().split())) for line in file.readlines()]
        
    return world