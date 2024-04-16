import { create } from 'zustand';

export const useStore = create(set => ({
  resultados: {},
  algoritmoActual: {},
  seleccionarAlgoritmoActual: (algoritmo) => set({ algoritmoActual: algoritmo }),
  guardarResultados: ({resultadosAlgoritmo}) => set({ resultados: resultadosAlgoritmo }),
}));