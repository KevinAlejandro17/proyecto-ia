import heapq
from .utils import reconstruir_ruta, calcular_costo

class Nodo:
    def __init__(self, estado, padre, operador, costo):
        self.estado = estado
        self.padre = padre
        self.operador = operador
        self.costo = costo

    def __lt__(self, other):
        return self.costo < other.costo

    def aplicar_operador(self, grid, operador):
        x, y = self.estado
        dx, dy = self.obtener_direccion(operador)
        nuevo_x, nuevo_y = x + dx, y + dy
        if 0 <= nuevo_x < 10 and 0 <= nuevo_y < 10 and grid[nuevo_x][nuevo_y] != 1:
            if self.padre is None or (nuevo_x, nuevo_y) != self.padre.estado:
                if self.padre and self.padre.padre and (nuevo_x, nuevo_y) == self.padre.padre.estado:
                    return self.estado
                return (nuevo_x, nuevo_y)
        return self.estado

    def obtener_direccion(self, operador):
        if operador == 'arriba':
            return (-1, 0)
        elif operador == 'abajo':
            return (1, 0)
        elif operador == 'izquierda':
            return (0, -1)
        elif operador == 'derecha':
            return (0, 1)

    def es_objetivo(self, grid):
        x, y = self.estado
        return grid[x][y] == 5

def costo_uniforme(grid, estado_inicial):
    pq = [(0, Nodo(estado_inicial, None, None, 0))]
    visitados = set()
    expandidos_con_padre = []
    solucion_encontrada = False
    costo_final = float('inf')

    while pq:
        costo, nodo = heapq.heappop(pq)
        if nodo.estado in visitados:
            continue
        visitados.add(nodo.estado)

        if nodo.es_objetivo(grid):
            if costo < costo_final:
                solucion_encontrada = True  
                costo_final = costo
                ruta = reconstruir_ruta(nodo)
            expandidos_con_padre.append((nodo, nodo.padre))
        else:
            for operador in ['arriba', 'abajo', 'izquierda', 'derecha']:
                nuevo_estado = nodo.aplicar_operador(grid, operador)
                if nuevo_estado != nodo.estado:
                    nuevo_costo = costo + calcular_costo(grid, nuevo_estado)
                    nuevo_nodo = Nodo(nuevo_estado, nodo, operador, nuevo_costo)
                    heapq.heappush(pq, (nuevo_costo, nuevo_nodo))
                    expandidos_con_padre.append((nuevo_nodo, nodo))

    if solucion_encontrada:
        path = ruta
        return path, [nodo for nodo in expandidos_con_padre if nodo[0].costo <= costo_final]
    else:
        return None, expandidos_con_padre