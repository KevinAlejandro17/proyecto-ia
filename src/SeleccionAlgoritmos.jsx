import React from "react";

import { useStore } from "./useStore";

const SeleccionAlgoritmos = () => {
  const algoritmos = [
    { nombre: 'Amplitud', id: 'amplitud' },
    { nombre: 'Profundidad', id: 'profundidad' },
    { nombre: 'Costo uniforme', id: 'costo' },
    { nombre: 'Avaro', id: 'avaro' },
    { nombre: 'A estrella', id: 'estrella' }
  ];

  const { seleccionarAlgoritmoActual } = useStore()

  return (
    <>
      <h4 className="text-2xl font-bold">Seleccionar algoritmo</h4>
      <div className="grid grid-cols-2 gap-4 mt-4">
        {
          algoritmos.map((algoritmo) => (
            <button 
              key={algoritmo.id} 
              className="px-3 py-1 rounded-lg bg-blue-900 w-36 col-span-1" 
              onClick={() => {seleccionarAlgoritmoActual(algoritmo)}}>
                
              {algoritmo.nombre}
            </button>
          ))
        }
      </div>
    </>
  );
};

export default SeleccionAlgoritmos;
