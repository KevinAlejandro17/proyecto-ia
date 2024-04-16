export const invertirSublistas = (path) => {
  if (!Array.isArray(path) || path.length === 0) {
    return path;
  }

  return path.map((sublista) => {
    if (!Array.isArray(sublista)) {
      return sublista;
    }
    return [...sublista].reverse();
  });
};

export const fetchData = async (algoritmoId) => {
  try {
    const fetchPath = `http://localhost:5000/${algoritmoId}`;
    const response = await fetch(fetchPath, {
      headers: {
        "Access-Control-Allow-Origin": "*",
      },
    });
    const data = await response.json();
    return {
      path: data,
    };
    /* return {
      path: data[0],
      nodos_expandidos: data[1],
      profundidad: data[2],
      tiempo_ejecucion: data[3],
    }; */
  } catch (error) {
    console.error(error);
  }
};

export const findStartPosition = (matrix) => {
  for (let row = 0; row < matrix.length; row++) {
      for (let col = 0; col < matrix[row].length; col++) {
          if (matrix[row][col] === 2) {
              return [row, col];
          }
      }
  }
  return null; // En caso de no encontrar un 2, deberías manejar este caso
}