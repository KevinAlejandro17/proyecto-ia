import React from "react";
import { useStore } from "./useStore";

const Resultados = () => {
  const { resultado } = useStore();

  return (
    <>
      <h4 className="text-2xl font-bold">Resultados</h4>

      <h6 className="text-lg font-semibold">Resultado: {resultado?.b}</h6>
    </>
  );
};

export default Resultados;