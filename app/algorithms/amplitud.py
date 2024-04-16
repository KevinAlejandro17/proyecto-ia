import heapq
from .utils import reconstruir_ruta, calcular_costo

class Nodo:
    def __init__(self, estado, padre, operador, profundidad, costo):
        self.estado = estado
        self.padre = padre
        self.operador = operador
        self.profundidad = profundidad
        self.costo = costo

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

def amplitud(grid, estado_inicial):
    cola = [Nodo(estado_inicial, None, None, 0, 0)]
    visitados = {}
    expandidos_con_padre = []
    solucion_encontrada = False
    profundidad_final = -1

    while cola:
        nodo = cola.pop(0)
        if nodo.estado in visitados:
            visitados[nodo.estado].append(nodo)
        else:
            visitados[nodo.estado] = [nodo]

        if nodo.es_objetivo(grid):
            if not solucion_encontrada:
                solucion_encontrada = True
                ruta, profundidad_final = reconstruir_ruta(nodo), nodo.profundidad
            expandidos_con_padre.append((nodo, nodo.padre))
        else:
            if solucion_encontrada and nodo.profundidad > profundidad_final:
                continue  # Descartar nodos que superan la profundidad de la solución
            for operador in ['arriba', 'abajo', 'izquierda', 'derecha']:
                nuevo_estado = nodo.aplicar_operador(grid, operador)
                if nuevo_estado != nodo.estado:
                    nuevo_costo = nodo.costo + calcular_costo(grid, nuevo_estado)
                    nuevo_nodo = Nodo(nuevo_estado, nodo, operador, nodo.profundidad + 1, nuevo_costo)
                    cola.append(nuevo_nodo)
                    expandidos_con_padre.append((nuevo_nodo, nodo))

    if solucion_encontrada:
        return ruta, profundidad_final, [nodo for nodo in expandidos_con_padre if nodo[0].profundidad <= profundidad_final]
    else:
        return None, -1, expandidos_con_padre