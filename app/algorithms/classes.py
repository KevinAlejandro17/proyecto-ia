class Nodo:
    def __init__(self, estado, padre, operador, costo, profundidad=0):
        self.estado = estado
        self.padre = padre
        self.operador = operador
        self.profundidad = profundidad
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